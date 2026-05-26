# 公众号已发布效果验收与工具顺手度横评

- 验收时间：2026-05-22 16:48:25
- 发表记录截图：`C:\html\published-review\published-list.png`
- 公开页截图目录：`C:\html\published-review`
- 规则：只看已发布公开页效果；不改后台已发布文章；本地发布版统一改为 `publish/wechat-standard.html`。

## 一、已发布文章效果排名

| 排名 | 标题 | 分数 | 图片 | 正文长度 | 主要问题 | 截图 |
|---:|---|---:|---:|---:|---|---|
| 1 | AnySearch / Tavily / Brave 实测：以后技术检索该怎么用 | 102 | 3 | 1837 | 无明显问题 | `01-anysearch-tavily-brave-实测-以后技术检索该怎么用-desktop.png`, `01-anysearch-tavily-brave-实测-以后技术检索该怎么用-mobile.png` |
| 2 | 四个 HTML Skill 横向对比：谁负责审美，谁负责文章，谁负责交付 | 88 | 4 | 2621 | 含表格，手机端风险较高 | `03-四个-html-skill-横向对比-谁负责审美-谁负责文章-谁负责交付-desktop.png`, `03-四个-html-skill-横向对比-谁负责审美-谁负责文章-谁负责交付-mobile.png` |
| 3 | 真实浏览器爬取方案重新评定 | 88 | 4 | 4308 | 含表格，手机端风险较高 | `05-真实浏览器爬取方案重新评定-desktop.png`, `05-真实浏览器爬取方案重新评定-mobile.png` |
| 4 | 我把 Codex 接到飞书后，最大的变化不是“手机能聊天” | 78 | 5 | 2568 | 分块感不足；含表格，手机端风险较高 | `04-我把-codex-接到飞书后-最大的变化不是-手机能聊天-desktop.png`, `04-我把-codex-接到飞书后-最大的变化不是-手机能聊天-mobile.png` |
| 5 | 比特、MoreLogin、AdsPower 三款指纹浏览器实测对比 | 78 | 5 | 5329 | 分块感不足；含表格，手机端风险较高 | `06-比特-morelogin-adspower-三款指纹浏览器实测对比-desktop.png`, `06-比特-morelogin-adspower-三款指纹浏览器实测对比-mobile.png` |
| 6 | 我本地跑了一遍 HTML-in-Canvas：能跑，但还远不是生产级 已修改 | 72 | 7 | 3502 | 分块感不足；发现疑似乱码或残缺关键词 | `02-我本地跑了一遍-html-in-canvas-能跑-但还远不是生产级-已修改-desktop.png`, `02-我本地跑了一遍-html-in-canvas-能跑-但还远不是生产级-已修改-mobile.png` |

## 二、最好样本标准

最好的是：**AnySearch / Tavily / Brave 实测：以后技术检索该怎么用**。
它胜出的原因不是标题，而是发布形态更接近公众号正确形态：
- 单列结构，图片不会横向并排。
- 正文图至少 3 张，且公开页图片能加载。
- 分段标题多，读者能扫读。
- 没有横向表格，手机端不容易压扁。
- 文字量控制在可读范围，适合公众号首发。

后续所有公众号发布版按这个标准收口：**单列长文 + PNG/JPG 信息图 + 内联样式 + 图片不裁剪 + 表格尽量改卡片 + 只保留一个发布入口**。

## 三、本地文章已按标准去重/统一入口

| Slug | 标准发布入口 | 字数 | 图片 | 表格 | 处理结论 |
|---|---|---:|---:|---:|---|
| anysearch-comparison | `C:\html\articles\anysearch-comparison\publish\wechat-standard.html` | 1898 | 3 | 0 | 合格 |
| browser-automation-methods | `C:\html\articles\browser-automation-methods\publish\wechat-standard.html` | 4375 | 3 | 1 | 仍有表格，下次发布前建议转卡片 |
| codex-feishu-bridge-control-plane | `C:\html\articles\codex-feishu-bridge-control-plane\publish\wechat-standard.html` | 2604 | 4 | 2 | 仍有表格，下次发布前建议转卡片 |
| html-in-canvas-review | `C:\html\articles\html-in-canvas-review\publish\wechat-standard.html` | 3548 | 6 | 0 | 合格 |
| html-skills-comparison | `C:\html\articles\html-skills-comparison\publish\wechat-standard.html` | 3054 | 3 | 1 | 仍有表格，下次发布前建议转卡片 |

旧版 HTML 已归档到各自 `publish/archive/`。以后发公众号只认：`C:\html\articles\<slug>\publish\wechat-standard.html`。

## 四、公众号场景工具顺手度

| 工具 | 本轮状态 | 适合位置 | 结论 |
|---|---|---|---|
| Playwright connectOverCDP | 成功 | 主流程 |  截图：`C:\html\published-review\tool-screenshots\01-playwright-connect-over-cdp.png` |
| OpenCLI | 成功 | 快速打开、state、临时查看 | URL: https://mp.weixin.qq.com/s/djui9wT8rs8sJEzaHxpoZg

url: https://mp.weixin.q 截图：`C:\html\published-review\tool-screenshots\02-opencli.png` |
| playwright-cli | 成功 | 探索/生成脚本，不适合作为固定登录态主流程 | 能截公开文章，但会启动独立浏览器；不适合公众号后台登录态任务。 截图：`C:\html\published-review\tool-screenshots\03-playwright-cli.png` |
| raw CDP | 成功 | 底层排障 | {"title":"AnySearch / Tavily / Brave 实测：以后技术检索该怎么用","imgs":3,"href":"https://mp. 截图：`C:\html\published-review\tool-screenshots\04-raw-cdp.png` |
| CDP Bridge MCP | 成功 | 桥在线时适合读当前标签页 | 桥服务启动后成功：可读当前真实 Chrome 标签页、执行 JS、截图；适合交互接管，长期批量仍不如 Playwright 脚本清晰。 截图：`C:\html\published-review\tool-screenshots\05-cdp-bridge-mcp.png` |

**最终主流程：Playwright connectOverCDP 接固定 Chrome `9223`。**
降级顺序：OpenCLI 快速确认 -> raw CDP 排障 -> CDP Bridge MCP/Chrome 插件做交互探索 -> playwright-cli 只用于探索和代码生成。

## 五、下一次发布前检查清单

- `publish/wechat-standard.html` 是唯一入口。
- 正文图不少于 3 张，PNG/JPG，单列展示。
- 不使用 `object-fit: cover`。
- 表格尽量改成卡片；必须保留表格时加 `table-layout: fixed`。
- 发表后从「发表记录」打开公开链接，保存手机/桌面截图。