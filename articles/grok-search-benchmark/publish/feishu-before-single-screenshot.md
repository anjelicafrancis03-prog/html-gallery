## 截图总览
以下三张图来自原 HTML 的关键页面，已前置，打开文档先看效果。
**截图 1：主 dashboard 全页**
<image token="Prl6bjXbEowd1CxDKaIce6p0n6e" width="1425" height="2669" align="center"/>

**截图 2：Grok MCP 视频生成实测**
<image token="RrkLb8ptOolj2PxpPS5cKidYnVp" width="1678" height="4207" align="center"/>

**截图 3：灰度运营经验收集专题**
<image token="VNhCbw1ndoJs9WxRk4wchUilnkf" width="1678" height="3528" align="center"/>

---

本轮测评聚焦中文长尾、平台规则、灰度运营、地方政策和开发者资料。重点观察是否能保留中文、是否找到中文原始来源、是否可核验、是否跑题，以及作为 Agent 工具的稳定性。**原 HTML 路径：** `C:\html\articles\grok-search-benchmark\index.html`
- 时间：2026-05-26
- 样本：10 个中文小众题材
- Grok MCP：release exe + UTF-8 自测通过
- 视频策略：480p 草稿，720p 终稿，10s 链式扩展
---

## 总评
**评分：7.6/10**Grok MCP 的优势不是传统网页 SERP，而是 X 语境、中文解释和灰度经验总结。它已经能稳定处理中文，但来源可信度需要 Bright Data 或内置搜索兜底。
> 最强场景：中文 AI 圈动态、X 上活跃的灰度运营经验、工具链趋势。最大风险：有时把 X 讨论当作事实，引用不是官方网页；一次长批量查询出现 ECONNRESET。
---

## 工具能力雷达
原 HTML 用 Chart.js 雷达图呈现。飞书文档里保留为同一组维度评分表，方便复制、检索和后续编辑。

<lark-table rows="5" cols="6" header-row="true" column-widths="122,122,122,122,122,122">

  <lark-tr>
    <lark-td>
      工具
    </lark-td>
    <lark-td>
      中文长尾
    </lark-td>
    <lark-td>
      来源可核验
    </lark-td>
    <lark-td>
      解释能力
    </lark-td>
    <lark-td>
      稳定性
    </lark-td>
    <lark-td>
      速度
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Grok MCP
    </lark-td>
    <lark-td>
      8
    </lark-td>
    <lark-td>
      6
    </lark-td>
    <lark-td>
      9
    </lark-td>
    <lark-td>
      6
    </lark-td>
    <lark-td>
      7
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Bright Data
    </lark-td>
    <lark-td>
      9
    </lark-td>
    <lark-td>
      9
    </lark-td>
    <lark-td>
      5
    </lark-td>
    <lark-td>
      9
    </lark-td>
    <lark-td>
      8
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Tavily
    </lark-td>
    <lark-td>
      7
    </lark-td>
    <lark-td>
      6
    </lark-td>
    <lark-td>
      7
    </lark-td>
    <lark-td>
      7
    </lark-td>
    <lark-td>
      8
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      内置搜索
    </lark-td>
    <lark-td>
      8
    </lark-td>
    <lark-td>
      8
    </lark-td>
    <lark-td>
      7
    </lark-td>
    <lark-td>
      8
    </lark-td>
    <lark-td>
      7
    </lark-td>
  </lark-tr>
</lark-table>

---

## 题材样本矩阵

<lark-table rows="11" cols="4" header-row="true" column-widths="183,183,183,183">

  <lark-tr>
    <lark-td>
      题材
    </lark-td>
    <lark-td>
      Grok MCP
    </lark-td>
    <lark-td>
      Bright Data
    </lark-td>
    <lark-td>
      Tavily / 内置搜索
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      AgentMemory / MCP / Codex / Windsurf
    </lark-td>
    <lark-td>
      强。中文 UTF-8 正常，能总结 AI Agent 技术栈，但引用多为 X。
    </lark-td>
    <lark-td>
      强。找到 HelloGitHub、Google ADK、awesome-mcp-zh 等中文/开源来源。
    </lark-td>
    <lark-td>
      中。返回 GitHub 和英文博客，速度快但中文质量一般。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      小红书蒲公英报备与限流
    </lark-td>
    <lark-td>
      中上。能给实操经验，但部分结论来自 X 逆向讨论。
    </lark-td>
    <lark-td>
      强。找到小红书蒲公英帮助中心、审核规范、行业文章。
    </lark-td>
    <lark-td>
      中。快，但容易混入泛运营文章。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      闲鱼批量上架 / 多店铺工具
    </lark-td>
    <lark-td>
      中。UTF-8 后能回答，但偏圈内经验，且可能引导到网盘资源，风险高。
    </lark-td>
    <lark-td>
      强。找到淘宝开放平台、第三方工具、腾讯云文章、B站经验。
    </lark-td>
    <lark-td>
      弱到中。容易把 R2 误解为其他领域。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      抖音小店无货源违规
    </lark-td>
    <lark-td>
      中上。能给风险判断，适合策略讨论。
    </lark-td>
    <lark-td>
      强。找到抖音搜索页、芒果店长、新闻和行业文章。
    </lark-td>
    <lark-td>
      中。速度快，但官方规则要另查。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞书多维表格 API
    </lark-td>
    <lark-td>
      中。解释清楚，但引用多来自 X。
    </lark-td>
    <lark-td>
      很强。官方飞书文档、开放平台 FAQ、CSDN 数据结构文章齐全。
    </lark-td>
    <lark-td>
      中上。能搜到文档，摘要可用。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      固定 Chrome CDP 9223 + Playwright
    </lark-td>
    <lark-td>
      中上。教程感强，符合实操，但有规避检测表述，需谨慎。
    </lark-td>
    <lark-td>
      中。中文官方 Playwright 资料能找，固定 Chrome 细节少。
    </lark-td>
    <lark-td>
      中。适合补教程。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      微信公众号转载 / 原创 / 白名单
    </lark-td>
    <lark-td>
      中。能解释机制，但需要微信官方社区核验。
    </lark-td>
    <lark-td>
      强。找到微信开放社区、编辑器教程、白名单说明。
    </lark-td>
    <lark-td>
      中。泛文章较多。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      跨境收款 Wise / Payoneer / Stripe
    </lark-td>
    <lark-td>
      中。能给选型建议，但金融合规需谨慎。
    </lark-td>
    <lark-td>
      强。Airwallex、Payoneer、Wise、Stripe 中文资料完整。
    </lark-td>
    <lark-td>
      中上。适合第一轮搜集。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      深圳灵活就业社保补贴
    </lark-td>
    <lark-td>
      中。能概括政策框架，但来源不是政府页。
    </lark-td>
    <lark-td>
      很强。直接找到深圳人社、罗湖区公示、PDF 名单。
    </lark-td>
    <lark-td>
      中。可做补充。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      中文开源 Agent Memory 本地向量检索
    </lark-td>
    <lark-td>
      未完成。一轮批量测试最后出现 ECONNRESET，记为稳定性风险。
    </lark-td>
    <lark-td>
      强。找到 awesome-mcp-zh、openEuler 本地混合检索、MCP Memory Service。
    </lark-td>
    <lark-td>
      中。能补博客和 GitHub。
    </lark-td>
  </lark-tr>
</lark-table>

---

## 当前样本详情
原 HTML 这里是可切换的交互详情区。为了在飞书中尽量保留结构，这里展开为全量静态样本详情。

<lark-table rows="5" cols="3" header-row="true" column-widths="244,244,244">

  <lark-tr>
    <lark-td>
      题材
    </lark-td>
    <lark-td>
      原交互详情区结论
    </lark-td>
    <lark-td>
      可核验来源
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      AgentMemory / MCP / Codex / Windsurf
    </lark-td>
    <lark-td>
      Grok 能把 AgentMemory、MCP、Codex、Windsurf、Antigravity 放进同一技术栈解释，适合趋势判断。
    </lark-td>
    <lark-td>
      https://github.com/521xueweihan/HelloGitHub/issues/3193https://github.com/yzfly/awesome-mcp-zh
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      小红书蒲公英报备与限流
    </lark-td>
    <lark-td>
      Grok 给出隐藏 level 字段、限流经验等社区视角；官方规则仍要用蒲公英帮助中心核验。
    </lark-td>
    <lark-td>
      https://pgy.xiaohongshu.com/help/docs?id=2908&userType=1https://www.xiao-ad.com/jd/1047.html
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      闲鱼批量上架 / 多店铺工具
    </lark-td>
    <lark-td>
      这类题材 Grok 能总结玩法，但合规性和安全性必须额外标红；不建议直接相信工具链接。
    </lark-td>
    <lark-td>
      https://developer.alibaba.com/docs/api.htm?apiId=69469https://www.kancloud.cn/xianyu888/xianyu_doc/2485187
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      抖音小店无货源违规
    </lark-td>
    <lark-td>
      Grok 的结论偏实际：纯无货源和批量铺货高风险，精选联盟和内容化更稳。
    </lark-td>
    <lark-td>
      https://www.mangoerp.com/erp/newsandtrends/detail/241https://www.douyin.com/search/%E6%8A%96%E9%9F%B3%E5%B0%8F%E5%BA%97%E6%97%A0%E8%B4%A7%E6%BA%90%E9%A3%8E%E9%99%A9%E6%8F%90%E7%A4%BA
    </lark-td>
  </lark-tr>
</lark-table>


<lark-table rows="5" cols="3" header-row="true" column-widths="244,244,244">

  <lark-tr>
    <lark-td>
      题材
    </lark-td>
    <lark-td>
      原交互详情区结论
    </lark-td>
    <lark-td>
      可核验来源
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      飞书多维表格 API
    </lark-td>
    <lark-td>
      开发文档类题材 Bright Data 更可靠，Grok 适合把字段类型和注意事项翻译成人话。
    </lark-td>
    <lark-td>
      https://open.feishu.cn/document/docs/bitable-v1/faq?lang=zh-CNhttps://www.feishu.cn/hc/zh-CN/articles/336307279050-%E5%A4%9A%E7%BB%B4%E8%A1%A8%E6%A0%BC-api-%E5%8A%9F%E8%83%BD%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      固定 Chrome CDP 9223 + Playwright
    </lark-td>
    <lark-td>
      Grok 很会写步骤，但涉及浏览器检测时要遵守验证和平台规则。
    </lark-td>
    <lark-td>
      https://playwright.nodejs.cn/
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      微信公众号转载 / 原创 / 白名单
    </lark-td>
    <lark-td>
      正式操作以微信后台和微信开放社区为准，Grok 适合做流程说明草稿。
    </lark-td>
    <lark-td>
      https://developers.weixin.qq.com/community/develop/doc/000820e3de0e00de3cc3fef2361800https://developers.weixin.qq.com/community/develop/doc/0008ae6541cc60903f05aadbb61400
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      跨境收款 Wise / Payoneer / Stripe
    </lark-td>
    <lark-td>
      涉及金融和税务时，Grok 不能单独作依据；需要官方费率、地区支持和合规条款。
    </lark-td>
    <lark-td>
      https://www.payoneer.com/zh-hans/b2b/https://www.airwallex.com/cn/blog/stripe-alternatives-2026
    </lark-td>
  </lark-tr>
</lark-table>


<lark-table rows="3" cols="3" header-row="true" column-widths="244,244,244">

  <lark-tr>
    <lark-td>
      题材
    </lark-td>
    <lark-td>
      原交互详情区结论
    </lark-td>
    <lark-td>
      可核验来源
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      深圳灵活就业社保补贴
    </lark-td>
    <lark-td>
      地方政策类 Bright Data 明显胜出，应该优先找政府域名和公示 PDF。
    </lark-td>
    <lark-td>
      http://hrss.sz.gov.cn/ztfw/gaojyzt/jycy/lhjysbbt/https://www.szlh.gov.cn/lhrlzyj/gkmlpt/content/12/12776/post_12776641.html
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      中文开源 Agent Memory 本地向量检索
    </lark-td>
    <lark-td>
      这个样本暴露了 Grok MCP 长批量调用仍需队列/重试机制；Bright Data 对中文开源资料更稳。
    </lark-td>
    <lark-td>
      https://github.com/yzfly/awesome-mcp-zhhttps://www.openeuler.org/zh/blog/20260318-MCP_01/20260318-MCP_01.html
    </lark-td>
  </lark-tr>
</lark-table>

---

## 截图证据与复现实验

<lark-table rows="4" cols="2" header-row="true" column-widths="350,350">

  <lark-tr>
    <lark-td>
      证据块
    </lark-td>
    <lark-td>
      内容
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Grok MCP 健康检查
    </lark-td>
    <lark-td>
      `grok-health.ok = true`，OAuth 已登录，执行路径为 release exe：`F:\codex\grok-cli\target\release\grok-cli.exe`
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      UTF-8 中文链路
    </lark-td>
    <lark-td>
      Node fetch 调 MCP，自测中文 query 原样回显，避免 PowerShell 把中文污染成问号。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Bright Data 取证
    </lark-td>
    <lark-td>
      SERP 能抓到官方文档、平台帮助中心、政府网站和中文长尾博客，适合作为事实核验层。
    </lark-td>
  </lark-tr>
</lark-table>

主 dashboard 截图已前置到文档开头，方便先看整体效果。
---

## Grok MCP 视频生成实测
### 参数

<lark-table rows="7" cols="2" header-row="true" column-widths="350,350">

  <lark-tr>
    <lark-td>
      参数
    </lark-td>
    <lark-td>
      值
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      工具
    </lark-td>
    <lark-td>
      `grok-video`
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      分辨率
    </lark-td>
    <lark-td>
      480p，省额度草稿模式
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      时长
    </lark-td>
    <lark-td>
      6 秒
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      比例
    </lark-td>
    <lark-td>
      16:9
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      耗时
    </lark-td>
    <lark-td>
      约 28.5 秒
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      模型
    </lark-td>
    <lark-td>
      `grok-imagine-video`
    </lark-td>
  </lark-tr>
</lark-table>

> 结论：Grok MCP 的视频生成链路已跑通，可以用于报告素材、短视频草稿和后续 10 秒分段扩展测试。视频实测截图已前置到文档开头；下方保留本地 MP4 文件作为原始证据。
---

## 最终建议

<lark-table rows="5" cols="3" header-row="true" column-widths="244,244,244">

  <lark-tr>
    <lark-td>
      任务类型
    </lark-td>
    <lark-td>
      推荐组合
    </lark-td>
    <lark-td>
      理由
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      中文平台规则核验
    </lark-td>
    <lark-td>
      Bright Data + 内置搜索
    </lark-td>
    <lark-td>
      优先找官方帮助中心、政府网站、微信开放社区、飞书文档等可核验来源。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      AI 工具链与 Agent 圈动态
    </lark-td>
    <lark-td>
      Grok MCP + Bright Data
    </lark-td>
    <lark-td>
      Grok 对 X 语境更敏感，Bright Data 负责用 GitHub、博客、文档核验。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      灰度运营经验收集
    </lark-td>
    <lark-td>
      Grok MCP + Tavily
    </lark-td>
    <lark-td>
      Grok 给经验总结，Tavily 快速补网页候选，最后人工筛风险。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      正式报告和可引用结论
    </lark-td>
    <lark-td>
      Bright Data + 内置搜索 + Grok 解释
    </lark-td>
    <lark-td>
      先证据、后解释。Grok 的口吻好，但不能单独当事实底座。
    </lark-td>
  </lark-tr>
</lark-table>

---

## 专题：灰度运营经验收集
### 定义边界
这里的“灰度运营经验”指平台规则边缘、非官方但广泛流传的实操经验，例如限流判断、批量发布节奏、账号权重、合作报备、工具链自动化。它只能作为线索，不能直接当成合规建议。
> 红线：不要收集、沉淀或执行绕过风控、规避审核、批量作弊、虚假交易、盗图搬运、验证码绕过等内容。
### 推荐组合
- **Grok MCP**：先找 X 上的近期讨论、逆向发现、圈内案例。
- **Tavily**：快速补中文网页、博客、新闻和行业文章。
- **Bright Data**：抓官方帮助中心、平台公告、政府 / 开放平台文档做核验。
### 风险标签
- **可用**：官方允许、公开文档支持、能长期复用。
- **待验证**：多人反馈但缺官方依据，只能小样本观察。
- **不要做**：明显绕规则、诱导封号、违法违规或侵犯权益。

<lark-table rows="6" cols="4" header-row="true" column-widths="183,183,183,183">

  <lark-tr>
    <lark-td>
      阶段
    </lark-td>
    <lark-td>
      操作
    </lark-td>
    <lark-td>
      工具
    </lark-td>
    <lark-td>
      产出
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1. 线索发现
    </lark-td>
    <lark-td>
      搜“平台名 + 症状 + 年份”，例如“小红书 报备 限流 2026”“抖店 无货源 违规 批量铺货”。
    </lark-td>
    <lark-td>
      Grok MCP / Tavily
    </lark-td>
    <lark-td>
      近期讨论、案例关键词、常见说法。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1. 来源分层
    </lark-td>
    <lark-td>
      把来源分成官方公告、平台帮助、行业媒体、个人经验、工具广告五类。
    </lark-td>
    <lark-td>
      Bright Data / 内置搜索
    </lark-td>
    <lark-td>
      可信度分层表。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1. 交叉验证
    </lark-td>
    <lark-td>
      每条经验至少找一个官方或准官方依据；找不到依据的只标为“待验证”。
    </lark-td>
    <lark-td>
      Bright Data scrape / 网页搜索
    </lark-td>
    <lark-td>
      证据链接和反例。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1. 风险落地
    </lark-td>
    <lark-td>
      把经验转成保守动作，例如减少模板重复、提高原创度、控制发布节奏、保留报备记录。
    </lark-td>
    <lark-td>
      Grok MCP 解释 + 人工判断
    </lark-td>
    <lark-td>
      低风险操作清单。
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      1. 复盘更新
    </lark-td>
    <lark-td>
      记录时间、平台版本、账号类型、样本量；过期经验自动降权。
    </lark-td>
    <lark-td>
      AgentMemory / 本地笔记
    </lark-td>
    <lark-td>
      可检索经验库。
    </lark-td>
  </lark-tr>
</lark-table>

### 采集模板
```plaintext
平台：小红书 / 抖音 / 闲鱼 / 微信 / 飞书
问题：限流、审核、报备、批量、接口、收款、账号权重
线索说法：一句话记录
来源类型：官方 / 行业 / 个人 / 工具广告
证据链接：至少 2 个
风险等级：可用 / 待验证 / 不要做
保守动作：转成不会伤号、不会违规的执行建议
更新时间：YYYY-MM-DD


```

灰度运营专题截图已前置到文档开头。
<view type="1">

  <file token="DJxhbSvBxo8d7jxpt4Ic455WnMh" name="grok-mcp-test-video-480p-6s.mp4"/>

</view>

