import fs from 'node:fs';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';

const outDir = 'C:/html/articles/browser-skill-mcp-review/assets';
const transport = new StdioClientTransport({
  command: 'cmd.exe',
  args: ['/c', 'npx', '-y', 'chrome-devtools-mcp@latest', '--browser-url=http://127.0.0.1:9223', '--slim', '--no-usage-statistics'],
  env: {
    ...process.env,
    CI: '1',
    CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS: '1',
    CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS: '1'
  }
});
const client = new Client({ name: 'codex-sdk-probe', version: '1.0.0' }, { capabilities: {} });
const report = { calls: [] };
async function call(name, args) {
  const res = await client.callTool({ name, arguments: args });
  report.calls.push({ name, args, content: res.content, structuredContent: res.structuredContent, isError: res.isError });
  return res;
}
try {
  await client.connect(transport);
  const tools = await client.listTools();
  report.toolNames = tools.tools.map(t => t.name);
  report.tools = tools.tools;
  if (report.toolNames.includes('navigate_page')) {
    await call('navigate_page', { url: 'http://127.0.0.1:4181/articles/browser-skill-mcp-review/index.html' });
  }
  if (report.toolNames.includes('evaluate_script')) {
    await call('evaluate_script', { function: '() => ({ title: document.title, h1: document.querySelector("h1")?.innerText, imgs: document.images.length, href: location.href })' });
  }
  if (report.toolNames.includes('take_screenshot')) {
    await call('take_screenshot', { filePath: `${outDir}/chrome-devtools-mcp-test.png`, fullPage: true });
  }
  fs.writeFileSync('C:/html/articles/browser-skill-mcp-review/chrome-devtools-mcp-sdk-probe.json', JSON.stringify(report, null, 2), 'utf8');
  console.log(JSON.stringify({ ok: true, toolNames: report.toolNames, calls: report.calls.map(c => ({ name: c.name, isError: c.isError, preview: JSON.stringify(c.content || c.structuredContent).slice(0, 600) })) }, null, 2));
} catch (error) {
  report.error = error.stack || error.message;
  fs.writeFileSync('C:/html/articles/browser-skill-mcp-review/chrome-devtools-mcp-sdk-probe.json', JSON.stringify(report, null, 2), 'utf8');
  console.error(error.stack || error.message);
  process.exitCode = 1;
} finally {
  try { await client.close(); } catch {}
}
