codex@f-codex:~/browser-stack$ scan --skills --mcp --evidence --keep-only-useful
[ COPY SUMMARY ]
+--- EXECUTIVE DECISION ---+ 2026-05-27
[OK] 本轮目标：继续寻找并测试类似浏览器操控 / 爬虫 / 网页抽取方向的 Skill、插件、MCP，筛出值得保留的工具。
# 浏览器自动化 Skill / MCP 可用性实测
一句话结论：现在本机最值得保留的是固定 Chrome + Node Playwright CDP + Playwright MCP + AnySearch；CDP Bridge 做补充；canghe 暂时备用；外部下一批重点测 Crawl4AI MCP / Firecrawl MCP / Browserbase MCP / mcp-chrome。
=== keep stack =====================================================
  * **主流程：** 固定 Chrome 9223 + Node Playwright connectOverCDP。
  * **验收层：** Playwright MCP，用来打开页面、抓 snapshot、看 console、做截图。
  * **资料层：** AnySearch，用来搜索和抽取公开网页正文。
  * **备用层：** canghe-url-to-markdown，适合借固定 Chrome 转 Markdown，但当前中文输出有乱码风险。
  * **候选层：** Crawl4AI MCP、Firecrawl MCP、Browserbase MCP、mcp-chrome，进入下一轮实测。


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
**anysearch**[KEEP]
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


[CORE] Fixed Chrome + Node Playwright CDProle=main
之前已经反复证明，这是最稳的主流程：固定 Chrome 保留登录态，Node Playwright 通过 9223 连接真实 Chrome，兼顾自动化能力和可调试性。
  * **固定地址：** `http://127.0.0.1:9223`。
  * **固定 profile：** `C:\Users\64998\\.opencli\chrome-profile`。
  * **保留建议：** 继续作为所有新线程的默认上网 / 登录 / 抓取基座。


+--- SCREENSHOT EVIDENCE ---+ rule=测评必须截图
[OK] 这次也按规则保留截图。任何后续横评 / 测评 / 实测，都必须有截图证据，不只写“我测了”。
![Playwright MCP 打开的浏览器经验教训页面截图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/playwright-mcp-page-check.png) Playwright MCP 验收截图：本地 HTTP 页面可打开、页面已加载、适合做视觉验收。 ![浏览器操控经验教训原始 HTML 预览截图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/browser-lessons-original.png) 原始经验教训 HTML 预览，用作本轮测试目标页面。 ![浏览器自动化工具排名概览图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/rank-overview-light.png) 之前 Chrome-only 横评资产：工具排序概览。 ![浏览器自动化工作流分层图](http://127.0.0.1:4181/articles/browser-skill-mcp-review/assets/workflow-layers-light.png) 之前 Chrome-only 横评资产：工作流分层，说明主控层 / 桥接层 / 抽取层边界。
+--- DECISION MATRIX ---+ scope=chrome+skills+mcp  
| 工具  | 定位  | 本轮状态  | 最适合任务  | 注意事项  |  
| --- | --- | --- | --- | --- |  
| 固定 Chrome + Node Playwright CDP  | 主控层  |  [OK] 已长期跑通  | 登录态页面、复杂点击、发布、截图、JS 执行  | 只连 9223；不要乱开临时 profile。  |  
| Playwright MCP  | 验收层  |  [OK] 已实测  | HTML 验收、console、snapshot、截图  | `file://` 受限，改走本地 HTTP。  |  
| CDP Bridge MCP  | 桥接层  |  [OK] 之前补测通过  | 扩展已在线时操控真实 Chrome session  | 18765/18766 在线不等于扩展已注册 session。  |  
| AnySearch  | 资料抽取层  |  [OK] 已实测  | 公开网页搜索、正文转 Markdown  | 不负责登录态浏览器交互。  |  
| canghe-url-to-markdown  | 备用抽取层  |  [WARN] 能跑但乱码  | 固定 Chrome 访问后转 Markdown  | 中文输出必须抽样检查。  |  
| Bright Data MCP  | 外部发现层  |  [OK] discover 可用  | 找新 MCP、查生态、做外部情报  | 不要把它当本地浏览器控制器。  |  
| Apify Skill  | 平台 Actor 层  |  [HYP] 读规则未运行  | 成熟平台 Actor、批量采集  | 需要 token、成本和合规边界。  |  
+--- NEXT CANDIDATES ---+ source=brightdata+local-inventory
[NEXT] Crawl4AI MCP
优先级高。它更接近“网页理解 + 抽取”的专业层，适合和 Playwright 主控互补。
[NEXT] Firecrawl MCP
优先级高。适合公开网页抓取、站点 crawl、转 Markdown，但要看额度和 API key。
[NEXT] mcp-chrome
值得试。目标是看它能否比 CDP Bridge 更少折腾地连上真实 Chrome。
[NEXT] Browserbase MCP
适合云浏览器，但可能涉及账号和付费。先免费额度小测，不替代本机固定 Chrome。
[NEXT] Playwright server variants
已有 Playwright MCP 可用，其他变体只测是否更稳定、更好截图、更好管理 session。
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
- AnySearch：可抽取公开网页 Markdown，适合资料层。
- canghe-url-to-markdown：能借固定 Chrome 转 Markdown，但中文输出有乱码风险。
- Bright Data MCP：适合发现外部候选。
- Apify skill：本机有，但需 token/额度/成本控制后再跑。

一句话结论：
现在本机最值得保留的是固定 Chrome + Node Playwright CDP + Playwright MCP + AnySearch；CDP Bridge 做补充；canghe 暂时备用；外部下一批重点测 Crawl4AI MCP / Firecrawl MCP / Browserbase MCP / mcp-chrome。

下一批优先测：
1. Crawl4AI MCP
2. Firecrawl MCP
3. mcp-chrome
4. Browserbase MCP
5. 其他 Playwright MCP server 变体

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

