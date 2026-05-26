# AnySearch 对比文章公众号封装注意事项

源文章：

```text
C:\html\articles\anysearch-comparison\index.html
```

预览：

```text
http://127.0.0.1:4174/articles/anysearch-comparison/index.html
```

## 核心原则

公众号版不要直接粘整页 HTML。网页母版里的 hero、grid、目录、响应式 CSS、阴影和横向表格，在公众号编辑器里容易丢样式或变形。

公众号最终稿应降级成：

```text
单列长文 + PNG 信息图 + 内联样式 + 原生段落结构
```

## 推荐公众号结构

1. 开头直接给结论：技术检索优先 AnySearch，Tavily 做第二搜索源。
2. 放第一张总览图：`assets/card-01-overview.png`。
3. 用短段落解释四个工具的分工。
4. 放第二张样本图：`assets/card-02-samples.png`。
5. 展开 3 到 5 个关键样本：CodeGraph benchmark、CVE-2024-3094、ngrok free domain、GPT Image 2 docs。
6. 放第三张工作流图：`assets/card-03-how-to-use.png`。
7. 结尾给其他 agent 的口令。

## 图片规则

- 使用 PNG/JPG，不用 SVG。
- 三张信息图单列纵向排列，每张独占一行。
- 不要横向并排。
- 不要用固定 16:9 裁剪。
- 不要使用 `object-fit: cover`。
- 图片显示应保持原比例。

可用正文图：

```text
C:\html\articles\anysearch-comparison\assets\card-01-overview.png
C:\html\articles\anysearch-comparison\assets\card-02-samples.png
C:\html\articles\anysearch-comparison\assets\card-03-how-to-use.png
```

## 表格处理

网页里的横向表格不建议原样搬到公众号。

建议改成四个工具卡片：

- AnySearch：主搜索源，适合 README、docs、benchmark、参数表。
- Tavily：第二搜索源，适合结构化结果和交叉验证。
- Brave：待接入，当前本机 API key/429 问题未完整实测。
- DeepSeek：解释层，不能当搜索工具。

如果保留表格，必须保证手机预览不被压扁；否则改为卡片。

## CSS 规则

公众号发布版要把关键 CSS 内联到 `style=""`。

保留：

- 字体栈：`-apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", Arial, sans-serif`
- 正文字号：16px 左右
- 行高：1.75 到 1.9
- 浅色背景块
- 1px 边框
- 小标题层级

删除：

- JS
- 目录跳转
- 悬浮控件
- 复杂 grid/flex
- 多列布局
- 动画

## 口令文本块

这段必须保留，并做成浅灰背景普通文本块，方便复制：

```text
用 anysearch + tavily 对比搜索：<主题>
要求：AnySearch 优先找 GitHub README / 官方 docs / 原始出处；Tavily 做第二搜索源；输出命中差异、关键 URL、结论和使用建议。
```

如果主题是具体技术项目，再加：

```text
注意避免重名项目，查询里带 owner/repo、官方域名、包名或关键 benchmark 数字。
```

## 封面

公众号封面不要直接用网页首屏截图。

建议单独做：

- 标题：`AnySearch 实测`
- 副标题：`技术检索该怎么用`
- 视觉：搜索源对比表 / 三步工作流
- 比例：`900x383` 或 `1200x510`

封面应放到：

```text
C:\html\articles\anysearch-comparison\imgs\
```

## 验收清单

发布前必须看手机预览：

- 标题是否过长。
- 三张信息图是否清楚。
- 工具对比是否被压扁。
- 口令文本是否能复制。
- 图片是否懒加载成功。
- 正文是否仍然是文章阅读体验，而不是网页 dashboard。

## 固定 Chrome 规则

如果进入公众号后台、使用登录态网页或浏览器发布，必须先验证固定 Chrome：

```powershell
& 'F:\codex\tools\verify-codex-fixed-chrome.ps1' -RestartIfMissingExtension
```

验证不通过时停止，不要新开普通 Chrome 顶替。
