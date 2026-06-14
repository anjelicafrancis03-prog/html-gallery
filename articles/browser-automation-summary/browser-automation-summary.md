# 浏览器自动化经验教训总结

一句话总结：以后浏览器自动化别到处换工具，主线固定为“固定 Chrome 9223 + Node Playwright CDP”，MCP 和抽取工具只做分层补充，所有测评必须截图留证。

## 最重要经验教训

1. 固定 Chrome 是根

`http://127.0.0.1:9223` 和 `C:\Users\64998\.opencli\chrome-profile` 是核心资产。

登录态、真实页面、发布流程、复杂点击，都优先走这个，不要乱用临时 profile。

2. Playwright CDP 是主力 API

真正稳定干活的是 Node Playwright API：

```js
const { chromium } = require('playwright');
const browser = await chromium.connectOverCDP('http://127.0.0.1:9223');
```

它适合长流程、截图、上传、DOM 抽取、JS 执行。

3. MCP 不是越多越好，要分层

现在值得保留：

- `Playwright MCP`：页面验收、snapshot、console、截图。
- `Google Chrome DevTools MCP`：官方 Chrome MCP，已连 9223 跑通。
- `CDP Bridge`：补充真实 tab 桥接，但别当唯一主线。
- `AnySearch`：公开网页搜索 / 正文抽取。
- `Crawl4AI Python`：网页转 Markdown / 截图，必须用专用 venv。

4. 不要被端口骗

`9223` 通，只说明 Chrome CDP 通。

`18765/18766` 通，只说明 CDP Bridge 服务在，不代表扩展 session 已注册。

OpenChrome 默认看 `9222`，和我们固定 `9223` 不一致。

5. 测评必须截图

以后所有“测评、横评、实测、benchmark”都必须有截图。

没截图就只能算“口头跑过”，不能进结论。

6. 本地 HTML 不要直接用 file:// 测

很多工具会限制 `file://`。

标准做法是启动本地 HTTP：

```powershell
python -m http.server 4181 --bind 127.0.0.1 --directory C:\html
```

7. Crawl4AI 不能装全局

它依赖 `lxml~=5.3`，会和本机其他工具冲突。

已建好专用入口：

```text
F:\codex\venvs\crawl4ai\Scripts\python.exe
```

8. 云工具没凭证不要伪测

Firecrawl、Browserbase、Apify 这类需要 key / 项目 ID / 额度。

没凭证就只能标记“入口确认，待凭证实测”，不能写成已跑通。

9. 不碰绕验证码和未授权访问

反爬、验证码、Cloudflare 绕过类宣传只能做风险识别，不做实操绕过。

我们只保留合规自动化、公开网页抽取、自己登录态页面操作。

10. 交接必须落盘

关键结论、截图、命令、路径都要写进 HTML 或 handoff。

当前主报告在：

```text
C:\html\articles\browser-skill-mcp-review\index.html
```

## 最终保留栈

固定 Chrome + Node Playwright CDP + Playwright MCP + Google Chrome DevTools MCP + AnySearch；CDP Bridge 做补充；Crawl4AI Python 进专用 venv；canghe 备用。

## 已落地的长期入口

已经按“API 核心 → CLI → MCP”的结构落地 `webctl`：

```text
F:\codex\webctl
```

常用命令：

```powershell
node F:\codex\webctl\src\cli.js start-chrome
node F:\codex\webctl\src\cli.js status
node F:\codex\webctl\src\cli.js registry
node F:\codex\webctl\src\cli.js screenshot C:\html\webctl-test.png --url https://example.com
```

MCP 入口：

```json
{
  "mcpServers": {
    "webctl-mcp": {
      "command": "node",
      "args": ["F:\\codex\\webctl\\src\\mcp.js"],
      "env": {
        "WEBCTL_CDP_URL": "http://127.0.0.1:9223"
      }
    }
  }
}
```

模块化规则：新工具先加到 `F:\codex\webctl\src\registry.js`，有截图和最小样本后再提升为 `keep`。

定期巡检：已创建每周一 09:30 的 `webctl 工具栈巡检` 自动化，只检查版本和候选，不自动安装、不写密钥。

## 分类口径

- `Playwright CDP`：API，不是 MCP，也不是 CLI。
- `Playwright MCP`：MCP，是 Agent 调用的工具层。
- `Google Chrome DevTools MCP`：MCP，是官方 Chrome DevTools 工具层。
- `playwright-cli` / `openchrome`：CLI，适合临时探路或一次性命令。

主线口径：固定 Chrome 9223 是浏览器底座；Playwright CDP API 是主力操控方式；MCP 是给 Agent 用的工具接口；CLI 是辅助探路。
