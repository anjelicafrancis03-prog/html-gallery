# 公众号大师交接：尽量保留 HTML 细节的发布办法

更新时间：2026-05-22

## 目标

把 `C:\html\articles\...` 里的 HTML 母版尽量保留到微信公众号草稿里。

核心判断：

- 公众号可以做“HTML 排版发布”，但不是完整浏览器。
- 知乎更像“内容转写”，公众号才值得投入保留 HTML 视觉细节。
- 目标不是保留 JS/交互，而是保留字体层级、色块、卡片、图片、段落节奏、表格和信息图。

## 推荐输入结构

每篇文章建议固定目录：

```text
C:\html\articles\<slug>\
  index.html                         # HTML 母版，完整可浏览
  assets\                            # 原始图片/信息图
  imgs\                              # 平台封面尺寸
  publish\
    <slug>-publish.html              # 公众号发布版，CSS 已处理
    wechat-cover.png                 # 公众号封面
    wechat-draft-inspect.json        # 草稿检查报告
    wechat-draft-current.png         # 草稿截图
```

## 公众号保留 HTML 的总路线

1. 先保留一个完整 HTML 母版。
   - 母版可以有完整 CSS、局部交互、辅助按钮、本地预览逻辑。
   - 文件放 `C:\html\articles\<slug>\index.html`。

2. 再生成公众号发布版 HTML。
   - 输出到 `publish\<slug>-publish.html`。
   - 所有关键 CSS 内联到元素 `style=""`。
   - 删除脚本、悬浮控件、主题切换、复杂交互。
   - 图片改成可上传的本地 PNG/JPG，避免 SVG 作为最终图。

3. 用固定 Chrome 登录态打开公众号编辑器。
   - 必须先执行固定 Chrome 验证：

```powershell
& 'F:\codex\tools\verify-codex-fixed-chrome.ps1' -RestartIfMissingExtension
```

   - 通过条件：`ok:true`、`browserType:extension`、固定 profile 为 `C:\Users\64998\.opencli\chrome-profile`、CDP 为 `http://127.0.0.1:9223`。
   - 验证失败就停止，不要开新浏览器顶替。

4. 通过公众号编辑器粘贴 HTML。
   - 优先用 `baoyu-post-to-wechat` 的 browser/article 工作流。
   - HTML 输入走 `--html <html_file>`，不要先转 Markdown。
   - 发布前只保存草稿，不点群发/发表，除非用户明确要求。

5. 上传封面和正文图片。
   - 封面用 `publish\wechat-cover.png`。
   - 正文图片必须确认已进入公众号素材/正文，不要只看本地 HTML。

6. 最后做真实验收。
   - 保存 `wechat-draft-inspect.json`。
   - 保存 `wechat-draft-current.png`。
   - 至少检查：标题、正文长度、图片数量、首屏、图片区、表格区、移动端窄屏预览。

## CSS 保留原则

公众号更容易保留这些：

- `font-size`
- `line-height`
- `font-weight`
- `color`
- `background-color`
- `padding`
- `margin`
- `border`
- `border-radius`
- `text-align`
- 简单 `display:block`
- 简单表格样式

公众号不可靠或不应依赖这些：

- JavaScript
- `position: fixed/sticky`
- 复杂 hover
- 复杂 grid/flex 自适应
- viewport 单位布局
- CSS 变量
- 外链字体
- 外链 CSS
- SVG 复杂图形
- iframe/video/canvas
- 依赖浏览器运行时的交互

处理办法：

- 发布版把 CSS 变量计算成具体值。
- 关键布局不要依赖复杂 grid，尽量变成单列纵向结构。
- 卡片和信息块可以保留，但不要嵌套太深。
- 复杂交互模块改成静态截图或信息图 PNG。

## 图片策略

这次 HTML 文章的经验必须继承：

1. 信息图单列纵向排列，不要三图横排。
2. 不要用 `aspect-ratio: 16 / 9` 加 `object-fit: cover` 裁信息图。
3. 信息图 CSS 应使用：

```css
.figure-card img {
  width: 100%;
  height: auto;
  object-fit: contain;
}
```

4. 浅色文章必须配浅色图片，不能把深色信息图硬塞进去。
5. 最终发布图优先 PNG/JPG，不要依赖 SVG。
6. 图片只承载一个结论，细节交给正文。
7. 中文信息图用本地字体生成，优先：

```python
ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", size=32)
ImageFont.truetype(r"C:\Windows\Fonts\msyhbd.ttc", size=48)
```

## HTML 转公众号发布版的具体处理

公众号发布版建议按这个顺序处理：

1. 读取 `index.html`。
2. 删除：
   - `<script>`
   - 页面主题切换按钮
   - 固定悬浮控件
   - hover-only 说明
   - 复杂交互 JS 依赖
3. 把 `<style>` 里的关键 CSS 内联到元素。
4. 把图片路径改成本地绝对路径或上传后素材 URL。
5. 把 SVG/Canvas/交互图转成 PNG。
6. 把横向多列图片区改成纵向单列。
7. 保留文章主结构：
   - H1/H2/H3
   - 段落
   - 引用
   - 表格
   - 信息图
   - 代码块或提示块
8. 输出 `publish\<slug>-publish.html`。

## 发布前检查清单

公众号大师接手时必须确认：

- [ ] 固定 Chrome 验证通过。
- [ ] 不是用临时浏览器。
- [ ] `index.html` 能通过 localhost 或本地服务正常打开。
- [ ] `publish\<slug>-publish.html` 存在。
- [ ] CSS 已内联，关键视觉不依赖外部 CSS。
- [ ] 图片都是 PNG/JPG，并已上传或可被上传。
- [ ] 封面图存在且比例适合公众号。
- [ ] 草稿保存后截图检查，不只看首屏。
- [ ] 不点击群发/发表，除非用户明确要求。

## 平台差异判断

公众号：

- 适合保留 HTML 视觉。
- 内联 CSS 有意义。
- 可以保留较多卡片、色块、图片和表格。

知乎：

- 不适合保留 HTML 原版式。
- 会转成知乎自己的 Draft 富文本结构。
- 更适合“内容转写 + 信息图插入”。

因此，同一篇 HTML 的平台策略：

```text
HTML 母版：完整设计和交互
公众号版：保留排版，CSS inline，交互静态化
知乎版：保留内容结构，关键视觉转 PNG
小红书/X/微博：按卡片或长图导出 PNG
```

## 给公众号大师的最短口令

如果只看一句：

> 公众号发布 HTML，不要追求 JS/交互，追求 inline CSS 后的静态阅读体验；复杂模块转 PNG，信息图单列不裁剪，固定 Chrome 验证通过后再进公众号编辑器，保存草稿后必须截图验收。

## 本次样例文章

样例目录：

```text
C:\html\articles\html-skills-comparison
```

已产出：

```text
C:\html\articles\html-skills-comparison\index.html
C:\html\articles\html-skills-comparison\publish\html-skills-comparison-publish.html
C:\html\articles\html-skills-comparison\publish\wechat-cover.png
C:\html\articles\html-skills-comparison\publish\wechat-draft-inspect.json
C:\html\articles\html-skills-comparison\publish\wechat-draft-current.png
```

可作为公众号 HTML 保留方案的参考样稿。
