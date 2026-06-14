---
url: http://127.0.0.1:4181/articles/browser-automation-lessons/index.html
title: "浏览器操控与爬虫工具经验教训总结"
captured_at: "2026-05-27T15:20:46.221Z"
---

# 浏览器操控与爬虫工具经验教训总结

Browser Automation Field Notes

## 浏览器操控与爬虫工具经验教训总结

这是一份给新线程、新电脑、新项目复用的工作底稿。它总结了固定 Chrome、Playwright CDP、CDP Bridge、OpenCLI、CloakBrowser、服务器选择和测评留证的关键经验。

## 核心结论

真正稳定的工作流，不是一次命令成功，而是能被别人接手、能复现、能留证据、能解释失败原因。

**第一条：**不要把“能打开网页”“能连端口”“能跑一次脚本”误认为已经形成稳定工作流。长期能用的东西必须有固定入口、验证命令、截图证据、失败判断和交接文档。

**第二条：**浏览器自动化的根是固定 Chrome。当前固定登录态 profile 是 \`C:\\Users\\64998\\.opencli\\chrome-profile\`，固定 CDP 是 \`http://127.0.0.1:9223\`。不要用普通 Chrome、临时 profile 或 Profile 1 替代。

**第三条：**\`9223\` 通，只说明 Chrome 原生 CDP 通，不说明插件、点击、CDP Bridge 都通。真实验收必须看完整链路。

**第四条：**所有测评、横评、实测、benchmark 必须截图。截图不是装饰，是证据。

## 三张图讲清楚工具分层

这些图来自之前的 Chrome-only 横评，适合直接给新线程做视觉索引。

## 工具定位

工具不是越多越好，关键是别混用职责。

主生产线

### Playwright CDP

用 \`chromium.connectOverCDP('http://127.0.0.1:9223')\` 连接固定 Chrome，负责长流程、截图、上传、等待、DOM/HTML/文本提取。

真实 tab 桥

### CDP Bridge

\`18765/18766\` 负责读当前真实标签页、执行 JS、截图。sessions 空不一定坏，可能只是扩展还没重连。

快刀

### OpenCLI

适合快开、快查、快抽。不要把它当成复杂数据生产线。

探索层

### playwright-cli

找 selector、试流程、看 iframe，再把结论沉淀到正式 Playwright 脚本。

排障层

### raw CDP

用于 \`/json/version\`、\`Runtime.evaluate\`、\`Page.captureScreenshot\` 等底层验证，不适合多人长期维护。

辅助

### Codex Chrome 插件

可做交互辅助，但不当主爬虫。插件可用不等于 CDP Bridge 可用。

## 测过和核查过的候选工具

宣传文案只能当线索，必须安装、跑最小例子、截图、记录版本和失败点。

| 工具 | 状态 | 结论 | 风险 |
| --- | --- | --- | --- |
| **Scrapegraph-ai** | 可研究 | AI 语义抽取思路有价值，但成本、速度、稳定性必须实测。 | Token 成本、动态页、结果可重复性。 |
| **rust-clawer** | 待测 | 文章存在，但公开仓库不可访问，不能正式推荐。 | 无源码、无可复现安装、无截图实测。 |
| **CloakBrowser** | 已装最小测试 | \`cloakbrowser 0.3.30\` 能打开 \`example.com\` 并截图，使用自带 Chromium。 | 高风险 anti-detect 工具，只做合规普通页面自动化评测。 |
| **BeautifulSoup / Regex / Trafilatura / Readability** | 基础工具 | 它们是内容抽取工具，不是 MCP，也不是浏览器操控工具。 | 适合静态页和正文抽取，不适合复杂登录态浏览器任务。 |

## 安全边界

能不能做和该不该做是两件事。工具越强，边界越要清楚。

**明确不做：**绕过 CAPTCHA、绕过 Cloudflare / Turnstile / reCAPTCHA、未授权访问、泄露 cookies/token/websocket URL、把明文 key 写进记忆或文档。

```
明文密钥只放：
.env
工具配置文件
Windows Credential Manager

记忆里只写：
工具名
用途
路径
登录状态
以后不要再问用户
```

## 服务器与网页部署经验

纯网页不要先买 VPS。先把部署问题做简单，再考虑服务器。

01

### Cloudflare Pages

纯静态网页、HTML 专题页、前端 App 的首选。免费、快、少维护。

02

### Cloudflare Workers

小 API、表单、webhook、轻量代理优先用它，别急着买 VPS。

03

### Oracle Always Free

真要 Linux VPS，优先试 Oracle 免费机，但注册和容量可能麻烦。

04

### Google e2-micro

Google Cloud 免费 VPS 是 e2-micro，小测试够用，不是强力 2 核。

**不建议某鱼 9.9 云账号：**容易遇到账号找回、IP 脏、NAT 限制、平台违规、跑路和无售后。纯网页更应该用 Cloudflare Pages。

## 以后做工具评测的固定顺序

不要只看 README，也不要只看一次命令成功。

```
1. 查真实性
2. 安装
3. 跑最小例子
4. 截图
5. 记录版本和路径
6. 说明适合场景
7. 说明风险和边界
8. 写入交接/记忆
```

## 给别的线程的最短交接稿

复制这段给新线程，就能让它先站在正确的地基上。

```
请先读取并遵守：
F:\codex\docs\browser-automation-handoff-2026-05-26.md
F:\codex\docs\browser-crawler-tool-inventory.md
F:\codex\docs\thread-operation-protocols.md

默认基座是固定 Chrome：
C:\Users\64998\.opencli\chrome-profile
http://127.0.0.1:9223

优先 Node Playwright connectOverCDP。
CDP Bridge 读当前真实 tab、执行 JS、截图。
OpenCLI 做快速 open/state/find/extract。
playwright-cli 做 selector 和流程探索。
raw CDP 只做底层排障。
Codex Chrome 插件只做交互辅助，不当主爬虫生产线。

验收前必须跑：
& 'F:\codex\tools\verify-codex-fixed-chrome.ps1' -RestartIfMissingExtension

测评、横评、实测、benchmark 必须截图，并报告截图路径。
不要打开普通 Chrome、临时 profile、Profile 1 来替代固定 Chrome。
不要清 cookies、不要移动登录态、不要泄露 token/cookie/websocket URL。
禁止把 CAPTCHA、Cloudflare、Turnstile、reCAPTCHA 或未授权访问绕过作为测试目标。
```