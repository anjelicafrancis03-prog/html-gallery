codex@f-codex:~/browser-stack$ scan --skills --mcp --evidence --keep-only-useful
[ COPY SUMMARY ]
+--- EXECUTIVE DECISION ---+ 2026-05-27
[OK] 本轮目标：继续寻找并测试类似浏览器操控 / 爬虫 / 网页抽取方向的 Skill、插件、MCP，筛出值得保留的工具。
# 浏览器自动化 Skill / MCP 可用性实测
一句话结论：现在本机最值得保留的是固定 Chrome + Node Playwright CDP + Playwright MCP + Google Chrome DevTools MCP + AnySearch；CDP Bridge 做补充；Crawl4AI Python 值得进独立 venv；canghe 暂时备用；Firecrawl / Browserbase 等云工具等凭证后再测。
=== keep stack =====================================================
  * **主流程：** 固定 Chrome 9223 + Node Playwright connectOverCDP。
  * **验收层：** Playwright MCP，用来打开页面、抓 snapshot、看 console、做截图。
  * **资料层：** AnySearch，用来搜索和抽取公开网页正文。
  * **备用层：** canghe-url-to-markdown，适合借固定 Chrome 转 Markdown，但当前中文输出有乱码风险。
  * **新增实测：** Google `chrome-devtools-mcp` 已连固定 9223 跑通 navigate / evaluate / screenshot；Crawl4AI Python 已抓取本地页并生成 Markdown + 截图。


+--- STATUS LEDGER ---+ exit=0
[OK]
### Playwright MCP
HTTP 页面打开、snapshot、console、截图已通过。
[OK]
### AnySearch
公开网页 extract 成 Markdown 已通过。
[WARN]
### canghe
能跑，但中文 Markdown 输出存在乱码。
[HYP]
### 外部候选
需下一轮安装和成本控制后测。
**fixed chrome + node pw**[CORE]
**playwright mcp**[KEEP]
**chrome devtools mcp**[KEEP]
**anysearch**[KEEP]
**crawl4ai python**[VENV]
**cdp bridge**[AUX]
**canghe url md**[CHECK]
**apify skill**[TOKEN]
[已实测](http://127.0.0.1:4181/articles/browser-skill-mcp-review/index.html#tested) [截图证据](http://127.0.0.1:4181/articles/browser-skill-mcp-review/index.html#screenshots) [横向矩阵](http://127.0.0.1:4181/articles/browser-skill-mcp-review/index.html#matrix) [下一批候选](http://127.0.0.1:4181/articles/browser-skill-mcp-review/index.html#candidates) [标准测试流程](http://127.0.0.1:4181/articles/browser-skill-mcp-review/index.html#workflow) [交接摘要](http://127.0.0.1:4181/articles/browser-skill-mcp-review/index.html#handoff)
+--- TESTED LOCALLY ---+ evidence=commands+screenshot
grep@tools:~$
[OK] Playwright MCProle=visual-check
本轮新暴露出 `mcp__playwright__` 工具组，已实测打开本地 HTTP 页面、读取可访问性快照、抓 console、截图。它适合做“测评必须截图”的验收层。
  * **强项：** 页面打开、点击、输入、snapshot、console、截图。
  * **限制：** 直接打开 `file://` 会被拦，建议统一走 `python -m http.server` 暴露到本地 HTTP。
  * **保留建议：** 保留。让新线程优先用它做 HTML 验收和截图。


[OK] AnySearch Skillrole=public-extract
读取了 `anysearch` skill 并运行 `extract https://example.com`，能把公开网页转成 Markdown。适合前期搜资料、读公开页面、为文章测评补素材。
  * **强项：** 公开网页正文抽取，输出轻，适合交给写作线程。
  * **限制：** 不是浏览器操控层，不负责登录态页面点击。
  * **保留建议：** 保留，作为搜索 / 抽取层。


[OK] Google Chrome DevTools MCProle=official-cdp
已用官方 MCP SDK 连接 `chrome-devtools-mcp@latest --browser-url=http://127.0.0.1:9223 --slim`，成功列出 `navigate / evaluate / screenshot`，并对本地报告页完成导航、执行 JS、截图。
  * **强项：** Google 官方维护，直接连固定 Chrome 9223，不需要扩展，适合 Antigravity / Gemini / Codex 等 MCP 客户端。
  * **限制：** `--slim` 只有 3 个工具；完整模式工具更多，但也更重。首次手写 stdio 探针会踩协议坑，建议用官方 SDK 或真实 MCP 客户端。
  * **保留建议：** 保留，并把它列为 Playwright MCP 之外的官方 Chrome MCP 备选。


[OK] Crawl4AI Pythonrole=markdown+crawl
已安装 `crawl4ai==0.8.6` 并运行 `crawl4ai-doctor`，健康检查通过；随后用 `AsyncWebCrawler` 抓取本地报告页，输出 7438 字符 Markdown 和截图。实测后已把全局 `lxml` 恢复到 6.x，后续必须给 Crawl4AI 单独建 venv。
  * **强项：** 中文 Markdown 输出干净，比 canghe 当前乱码结果更可靠；适合公开页抽取、长文转 Markdown、截图留证。
  * **风险：** Crawl4AI 要 `lxml~=5.3`，但本机其他工具需要 `lxml>=6.0.0`；全局安装会互相打架。
  * **保留建议：** 保留，但以后必须放独立 venv 或 uv 项目，不再污染全局 Python。


[WARN] canghe-url-to-markdownrole=chrome-md
已用固定 Chrome 抓取当前本地 HTML，并输出到 `C:\html\articles\browser-automation-lessons\canghe-capture.md`。流程能跑，但中文内容出现乱码，不能当无脑主力。
  * **强项：** 能借固定 Chrome 访问页面后转 Markdown。
  * **风险：** 中文编码需要复核，特别是公众号 / 知乎类长文。
  * **保留建议：** 备用。每次输出必须抽样看中文。


[HYP] Bright Data MCProle=discover
已用 Bright Data MCP 做外部候选发现，找到了 Browserbase MCP、mcp-chrome、Crawl4AI MCP、Firecrawl MCP、Playwright MCP server 变体等方向。
  * **强项：** 发现工具、补外部情报、查生态。
  * **限制：** 不是本地 Chrome 主控工具。
  * **保留建议：** 保留为发现层，不替代 Playwright。


[TOKEN] Apify Skillrole=actor-platform
本机有 Apify competitor intelligence 相关 skill，已读规则但未直接跑 actor。原因是它涉及平台 token、额度、运行成本，必须单独做限额测试。
  * **强项：** 成熟 Actor 生态，适合平台级抓取任务。
  * **风险：** 成本、token、目标站合规边界。
  * **保留建议：** 列入后续测评，先小样本、低额度。


[BLOCKED] Firecrawl / Browserbaserole=cloud-api
已确认 `firecrawl-mcp@3.17.0` 和 `@browserbasehq/mcp@3.0.0` 的入口。当前本机没有 `FIRECRAWL_API_KEY / FIRECRAWL_API_URL / BROWSERBASE_API_KEY / BROWSERBASE_PROJECT_ID` 环境变量，因此不做伪实测。
  * **Firecrawl：** 需要 API key 或自托管 URL；适合公开网页 scrape / crawl。
  * **Browserbase：** 需要云账号和项目 ID；适合云浏览器 session，不替代本机固定 Chrome。
  * **保留建议：** 等凭证齐了再小样本跑，先设预算和截图规则。


[WARN] OpenChrome MCProle=port-mismatch
`openchrome-mcp@1.12.5` 的 CLI 很完整，但 `doctor / navigate` 默认检查 9222；我们的固定 Chrome 是 9223，所以快捷命令直接失败。`serve -p 9223` 理论可接，但没有必要替代已跑通的官方 Chrome DevTools MCP。
  * **强项：** one-shot 命令多，适合脚本化浏览器动作。
  * **风险：** 默认 9222 和本机固定 9223 不一致；还包含绕验证宣传，合规边界要收紧。
  * **保留建议：** 暂不主推，后续只测 `serve -p 9223` 的普通自动化能力。


[CORE] Fixed Chrome + Node Playwright CDProle=main
之前已经反复证明，这是最稳的主流程：固定 Chrome 保留登录态，Node Playwright 通过 9223 连接真实 Chrome，兼顾自动化能力和可调试性。
  * **固定地址：** `http://127.0.0.1:9223`。
  * **固定 profile：** `C:\Users\64998\\.opencli\chrome-profile`。
  * **保留建议：** 继续作为所有新线程的默认上网 / 登录 / 抓取基座。


+--- SCREENSHOT EVIDENCE ---+ rule=测评必须截图
[OK] 这次也按规则保留截图。任何后续横评 / 测评 / 实测，都必须有截图证据，不只写“我测了”。
![Playwright MCP 打开的浏览器经验教训页面截图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/playwright-mcp-page-check.png) Playwright MCP 验收截图：本地 HTTP 页面可打开、页面已加载、适合做视觉验收。 ![Google Chrome DevTools MCP 连接固定 Chrome 后截图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/chrome-devtools-mcp-test.png) Google Chrome DevTools MCP 实测截图：通过 `--browser-url=http://127.0.0.1:9223 --slim` 连接固定 Chrome，完成 navigate / evaluate / screenshot。 ![Crawl4AI 抓取本地报告页截图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/crawl4ai-local-page.png) Crawl4AI Python 实测截图：`AsyncWebCrawler` 抓取同一页，输出 Markdown 和截图，中文 Markdown 正常。 ![浏览器操控经验教训原始 HTML 预览截图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/browser-lessons-original.png) 原始经验教训 HTML 预览，用作本轮测试目标页面。 ![浏览器自动化工具排名概览图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/rank-overview-light.png) 之前 Chrome-only 横评资产：工具排序概览。 ![浏览器自动化工作流分层图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/workflow-layers-light.png) 之前 Chrome-only 横评资产：工作流分层，说明主控层 / 桥接层 / 抽取层边界。
+--- DECISION MATRIX ---+ scope=chrome+skills+mcp  
| 工具  | 定位  | 本轮状态  | 最适合任务  | 注意事项  |  
| --- | --- | --- | --- | --- |  
| 固定 Chrome + Node Playwright CDP  | 主控层  |  [OK] 已长期跑通  | 登录态页面、复杂点击、发布、截图、JS 执行  | 只连 9223；不要乱开临时 profile。  |  
| Playwright MCP  | 验收层  |  [OK] 已实测  | HTML 验收、console、snapshot、截图  | `file://` 受限，改走本地 HTTP。  |  
| Google Chrome DevTools MCP  | 官方 CDP MCP  |  [OK] 已连 9223 实测  | 官方 MCP 客户端接入、导航、JS 执行、截图  | 建议 `--browser-url=http://127.0.0.1:9223 --slim --no-usage-statistics` 起步。  |  
| CDP Bridge MCP  | 桥接层  |  [OK] 之前补测通过  | 扩展已在线时操控真实 Chrome session  | 18765/18766 在线不等于扩展已注册 session。  |  
| AnySearch  | 资料抽取层  |  [OK] 已实测  | 公开网页搜索、正文转 Markdown  | 不负责登录态浏览器交互。  |  
| Crawl4AI Python  | 网页抽取 / Markdown  |  [OK] doctor + 本地页抓取通过  | 公开页抽取、Markdown、截图、批量 crawl 基座  | 必须独立 venv；全局 `lxml` 已恢复 6.x，Crawl4AI 不能继续放全局。  |  
| Crawl4AI MCP  | MCP 包装层  |  [WAIT] 缺本地 server  | 把 Crawl4AI Server 暴露给 MCP 客户端  | 需要 Docker daemon 或手动启动 11235 Crawl4AI Server。  |  
| canghe-url-to-markdown  | 备用抽取层  |  [WARN] 能跑但乱码  | 固定 Chrome 访问后转 Markdown  | 中文输出必须抽样检查。  |  
| Bright Data MCP  | 外部发现层  |  [OK] discover 可用  | 找新 MCP、查生态、做外部情报  | 不要把它当本地浏览器控制器。  |  
| Apify Skill  | 平台 Actor 层  |  [HYP] 读规则未运行  | 成熟平台 Actor、批量采集  | 需要 token、成本和合规边界。  |  
| Firecrawl MCP  | 云 scrape / crawl  |  [WAIT] 缺 API key 或自托管 URL  | 公开网页 scrape、crawl、页面交互  | `firecrawl-mcp` 启动即要求 `FIRECRAWL_API_KEY` 或 `FIRECRAWL_API_URL`。  |  
| Browserbase MCP  | 云浏览器  |  [WAIT] 缺云账号凭证  | 云端浏览器 session、远程运行  | 需要 `BROWSERBASE_API_KEY` 和 `BROWSERBASE_PROJECT_ID`。  |  
| OpenChrome MCP  | 真实 Chrome MCP 候选  |  [WARN] 默认 9222 不合拍  | one-shot 浏览器动作、脚本化场景  | 默认查 9222；本机固定 Chrome 是 9223，需显式 `serve -p 9223` 再测。  |  
+--- NEXT CANDIDATES ---+ source=brightdata+local-inventory
[WAIT] Crawl4AI MCP
入口确认：`mcp-crawl4ai-ts@3.0.2`。阻塞原因：它需要正在运行的 Crawl4AI Server，默认 `http://localhost:11235`；本机 Docker daemon 当前没启动，11235 也没服务。
[WAIT] Firecrawl MCP
入口确认：`firecrawl-mcp@3.17.0`。启动时明确要求 `FIRECRAWL_API_KEY` 或 `FIRECRAWL_API_URL`，当前本机都没有。
[NEXT] @pyrokine/mcp-chrome
入口确认：`@pyrokine/mcp-chrome@2.0.2`。它有扩展模式和 CDP 模式；后续只测普通自动化能力，跳过 anti-detection / CAPTCHA 相关宣传。
[WAIT] Browserbase MCP
入口确认：`@browserbasehq/mcp@3.0.0`。需要 Browserbase 云账号和项目凭证；定位是云浏览器，不替代本机固定 Chrome。
[KEEP] Google Chrome DevTools MCP
已实测通过，优先级上升。它是 Google 官方 MCP，适合交给 Antigravity / Gemini / Codex 等支持 MCP 的新线程。
[SKIP] 反验证码绕过类
不测绕过 CAPTCHA / Cloudflare / 未授权访问。只做合规网页自动化、登录态自用、公开页面抽取。
+--- STANDARD TEST PROTOCOL ---+ for=new-thread
以后别的线程测试同类工具，照这个标准走，结果才可比：
  1. **确认工具入口：** skill 路径、MCP 名称、命令、端口、是否需要 token。
  2. **跑公开页：** 先用 `https://example.com` 或公开文章页，确认基础访问和抽取。
  3. **跑本地 HTML：** 用 `python -m http.server` 暴露 `C:\html`，避免 `file://` 限制。
  4. **执行 JS：** 至少拿 `document.title`、`location.href`、正文前 500 字。
  5. **截图：** 测评必须截图，保存到当前文章 `assets` 或同级目录。
  6. **看 console：** 记录有没有 404、跨域、资源加载失败。
  7. **写结论：** 必须说明“适合什么、不适合什么、是否保留、下一步怎么测”。



```
pw@chrome:~$ node -e "const { chromium } = require('playwright'); /* connectOverCDP 9223 */"
mcp@playwright:~$ browser_navigate http://127.0.0.1:4181/articles/...
mcp@playwright:~$ browser_snapshot && browser_take_screenshot
search@anysearch:~$ python anysearch_cli.py extract https://example.com
md@canghe:~$ npx -y bun main.ts URL -o output.md
report@html:~$ save C:\html\articles\browser-skill-mcp-review\index.html
```

+--- COPYABLE HANDOFF ---+ paste=next-thread
给新线程的短交接：

```
请继续浏览器自动化 / 爬虫工具横评，但范围限定为 Chrome、Skill、插件、MCP，不要再混入比特浏览器、AdsPower、MoreLogin。

当前已验证基座：
- 固定 Chrome：C:\Program Files\Google\Chrome\Application\chrome.exe
- 固定 profile：C:\Users\64998\.opencli\chrome-profile
- 固定 CDP：http://127.0.0.1:9223
- Node Playwright 已可用，优先用 chromium.connectOverCDP('http://127.0.0.1:9223')

本轮新增已测：
- Playwright MCP：可打开本地 HTTP 页面、snapshot、console、截图；file:// 受限，改用 python -m http.server。
- Google Chrome DevTools MCP：官方 ChromeDevTools 项，已用 `--browser-url=http://127.0.0.1:9223 --slim` 连固定 Chrome，跑通 navigate / evaluate / screenshot。
- AnySearch：可抽取公开网页 Markdown，适合资料层。
- Crawl4AI Python：`crawl4ai==0.8.6` 已实测通过，本地报告页抓取成功，输出 Markdown 和截图；但全局环境已把 `lxml` 恢复到 6.x，后续必须迁到独立 venv，因为 Crawl4AI 要 `lxml~=5.3`。
- canghe-url-to-markdown：能借固定 Chrome 转 Markdown，但中文输出有乱码风险。
- Bright Data MCP：适合发现外部候选。
- Apify skill：本机有，但需 token/额度/成本控制后再跑。
- Firecrawl MCP / Browserbase MCP：入口已确认，但本机缺 API key/项目凭证，暂不伪实测。
- Crawl4AI MCP：`mcp-crawl4ai-ts` 需要本地 Crawl4AI Server；当前 Docker daemon 未启动，11235 无服务。
- OpenChrome MCP：CLI 可用但默认查 9222；本机固定 Chrome 是 9223，快捷命令失败，后续只测 `serve -p 9223`。

一句话结论：
现在本机最值得保留的是固定 Chrome + Node Playwright CDP + Playwright MCP + Google Chrome DevTools MCP + AnySearch；CDP Bridge 做补充；Crawl4AI Python 值得进独立 venv；canghe 暂时备用；Firecrawl / Browserbase 等云工具等凭证后再测。

下一批优先测：
1. 把 Crawl4AI 迁到独立 venv / uv 项目，修复全局 lxml 冲突。
2. 启动 Docker 后拉起 Crawl4AI Server，再测 mcp-crawl4ai-ts。
3. 配好 Firecrawl / Browserbase 凭证后做小样本截图测评。
4. 测 @pyrokine/mcp-chrome 的普通 CDP/扩展模式。
5. OpenChrome 只测 serve -p 9223，不再用默认 9222 快捷命令下结论。

硬规则：
- 任何测评、横评、实测都必须截图。
- 不测试绕过 CAPTCHA / Cloudflare / 未授权访问。
- 每个工具必须给：截图、输入、输出、适合任务、不适合任务、是否保留。
```

[ COPY HANDOFF ] [ COPY TEST PROTOCOL ]

```
标准测试流程：
1. 启动或确认固定 Chrome 9223。
2. 如果测 HTML，先用 python -m http.server --bind 127.0.0.1 --directory C:\html 4181。
3. 工具打开同一公开 URL 和同一本地 URL。
4. 抓 document.title、location.href、正文摘要。
5. 截图保存。
6. 读取 console 或错误日志。
7. 写入横评表：定位、状态、优点、限制、是否保留。
```

