const fs = await import("node:fs/promises");
const { spawn } = await import("node:child_process");
const { mkdtemp, rm } = await import("node:fs/promises");
const os = await import("node:os");
const path = await import("node:path");

const chrome = "F:\\codex\\tools\\chrome-for-testing-canary\\chrome-win64\\chrome.exe";
const url = "http://127.0.0.1:4174/articles/wechat-automation-tools/index.html";
const outDir = "C:\\html\\articles\\wechat-automation-tools\\assets";
const port = 9366;

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function getJson(endpoint) {
  const response = await fetch(`http://127.0.0.1:${port}${endpoint}`);
  if (!response.ok) throw new Error(`${endpoint}: ${response.status}`);
  return response.json();
}

async function waitPage() {
  for (let i = 0; i < 40; i++) {
    try {
      const tabs = await getJson("/json/list");
      const page = tabs.find(tab => tab.type === "page");
      if (page) return page;
    } catch {}
    await sleep(250);
  }
  throw new Error("page not ready");
}

async function withSocket(wsUrl, fn) {
  const socket = new WebSocket(wsUrl);
  let id = 0;
  const pending = new Map();

  socket.addEventListener("message", event => {
    const msg = JSON.parse(event.data.toString());
    if (msg.id && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(new Error(JSON.stringify(msg.error)));
      else resolve(msg.result);
    }
  });

  await new Promise((resolve, reject) => {
    socket.addEventListener("open", resolve, { once: true });
    socket.addEventListener("error", reject, { once: true });
  });

  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const msgId = ++id;
    pending.set(msgId, { resolve, reject });
    socket.send(JSON.stringify({ id: msgId, method, params }));
  });

  try {
    return await fn(send);
  } finally {
    socket.close();
  }
}

async function capture(width, height, filename) {
  const page = await waitPage();
  return withSocket(page.webSocketDebuggerUrl, async send => {
    await send("Page.enable");
    await send("Runtime.enable");
    await send("Emulation.setDeviceMetricsOverride", {
      width,
      height,
      deviceScaleFactor: 1,
      mobile: width < 600,
    });
    await send("Page.navigate", { url });
    await sleep(1600);
    const metricsResult = await send("Runtime.evaluate", {
      returnByValue: true,
      expression: `({
        title: document.title,
        innerWidth: window.innerWidth,
        bodyWidth: document.body.clientWidth,
        scrollWidth: document.documentElement.scrollWidth,
        imageCount: document.images.length,
        imagesOk: Array.from(document.images).every(img => img.complete && img.naturalWidth > 0),
        hasQuestionMarks: document.body.innerText.includes('????'),
        heroImg: document.querySelector('.hero-card img')?.getAttribute('src')
      })`,
    });
    const screenshot = await send("Page.captureScreenshot", { format: "png", fromSurface: true });
    await fs.writeFile(path.join(outDir, filename), Buffer.from(screenshot.data, "base64"));
    return metricsResult.result.value;
  });
}

const profile = await mkdtemp(path.join(os.tmpdir(), "wechat-tools-verify-"));
const proc = spawn(chrome, [
  `--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`,
  "--headless=new",
  "--disable-gpu",
  "about:blank",
], { stdio: "ignore" });

try {
  const desktop = await capture(1280, 720, "verify-desktop.png");
  const mobile = await capture(390, 844, "verify-mobile.png");
  const report = { desktop, mobile };
  await fs.writeFile(path.join(outDir, "verify-report.json"), JSON.stringify(report, null, 2), "utf8");
  console.log(JSON.stringify(report, null, 2));
} finally {
  proc.kill();
  await new Promise(resolve => proc.once("exit", resolve));
  await sleep(500);
  try {
    await rm(profile, { recursive: true, force: true });
  } catch {
    // Chrome may keep a lockfile briefly after exit on Windows; verification has already completed.
  }
}
