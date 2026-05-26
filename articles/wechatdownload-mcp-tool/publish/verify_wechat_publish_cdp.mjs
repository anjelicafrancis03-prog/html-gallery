const fs = await import("node:fs/promises");
const { spawn } = await import("node:child_process");
const { mkdtemp, rm } = await import("node:fs/promises");
const os = await import("node:os");
const path = await import("node:path");

const chrome = "F:\\codex\\tools\\chrome-for-testing-canary\\chrome-win64\\chrome.exe";
const url = "http://127.0.0.1:4174/articles/wechatdownload-mcp-tool/publish/wechat-standard.html";
const outDir = "C:\\html\\articles\\wechatdownload-mcp-tool\\publish";
const port = 9368;

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

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
      deviceScaleFactor: width < 600 ? 2 : 1,
      mobile: width < 600,
    });
    await send("Page.navigate", { url });
    await sleep(1800);
    const metrics = await send("Runtime.evaluate", {
      returnByValue: true,
      expression: `(() => {
        const imgs = Array.from(document.images);
        const srcs = imgs.map(img => img.getAttribute('src'));
        const inlineStyleText = Array.from(document.querySelectorAll('[style]')).map(el => el.getAttribute('style') || '').join('\\n');
        return {
          title: document.title,
          innerWidth: window.innerWidth,
          bodyWidth: Math.round(document.body.getBoundingClientRect().width),
          scrollWidth: document.documentElement.scrollWidth,
          imageCount: imgs.length,
          imagesOk: imgs.every(img => img.complete && img.naturalWidth > 0),
          hasQuestionMarks: document.body.innerText.includes('????'),
          hasStyleTag: Boolean(document.querySelector('style')),
          usesObjectFitCoverStyle: inlineStyleText.includes('object-fit: cover'),
          includesLongIndexImage: srcs.some(src => (src || '').includes('01-quanlitu-index-page')),
          commandBlocks: Array.from(document.querySelectorAll('section')).filter(el => (el.getAttribute('style') || '').includes('white-space:pre-wrap')).length,
          h2Count: document.querySelectorAll('h2').length,
          textLength: document.body.innerText.length
        };
      })()`,
    });
    const shot = await send("Page.captureScreenshot", {
      format: "png",
      fromSurface: true,
      captureBeyondViewport: true,
    });
    await fs.writeFile(path.join(outDir, filename), Buffer.from(shot.data, "base64"));
    return metrics.result.value;
  });
}

const profile = await mkdtemp(path.join(os.tmpdir(), "wechatdownload-publish-verify-"));
const proc = spawn(chrome, [
  `--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`,
  "--headless=new",
  "--disable-gpu",
  "about:blank",
], { stdio: "ignore" });

try {
  const desktop = await capture(1280, 1200, "verify-wechat-publish-desktop.png");
  const mobile = await capture(390, 1000, "verify-wechat-publish-mobile.png");
  const report = { desktop, mobile };
  await fs.writeFile(path.join(outDir, "verify-wechat-publish-report.json"), JSON.stringify(report, null, 2), "utf8");
  console.log(JSON.stringify(report, null, 2));
} finally {
  proc.kill();
  await new Promise(resolve => proc.once("exit", resolve));
  await sleep(500);
  try {
    await rm(profile, { recursive: true, force: true });
  } catch {}
}
