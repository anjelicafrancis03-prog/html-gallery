# HTML-in-Canvas 专用 Canary 工作流

用途：本地预览需要 HTML-in-Canvas / `drawElementImage()` / WebGL `texElementImage2D()` / WebGPU `copyElementImageToTexture()` 的实验效果。

## 结论

可以固定成“本地专用预览浏览器”，但不能当成普通用户生产浏览器。

原因：

- 普通 Chrome 148 实测 API 是 `undefined`。
- Chrome for Testing Canary 150 + `chrome://flags/#canvas-draw-element` 实测可用。
- 该能力仍是 Chromium 实验项，不能假设用户浏览器可用。

## 固定入口

启动烟测：

```powershell
& 'C:\html\tools\open-html-in-canvas.ps1'
```

打开指定本地 app：

```powershell
& 'C:\html\tools\open-html-in-canvas.ps1' -Url 'http://127.0.0.1:5173/'
```

如果 app 自己已经有服务，不需要启动 `C:\html` 静态服务：

```powershell
& 'C:\html\tools\open-html-in-canvas.ps1' -Url 'http://127.0.0.1:5173/' -NoServer
```

## 固定配置

- Canary：`F:\codex\tools\chrome-for-testing-canary\chrome-win64\chrome.exe`
- Profile：`F:\codex\experiments\html-in-canvas\canary-fixed-profile`
- 实验项：`canvas-draw-element@1`
- 调试端口：`http://127.0.0.1:9344`
- 默认静态根目录：`C:\html`
- 默认本地服务：`http://127.0.0.1:4174`

## 和固定 Chrome 的边界

这个 Canary 只用于实验渲染，不保存公众号、知乎、小红书等登录态。

登录态网页、远程网站、公众号后台仍然必须先跑固定 Chrome 验证：

```powershell
& 'F:\codex\tools\verify-codex-fixed-chrome.ps1' -RestartIfMissingExtension
```

不要把 HTML-in-Canvas Canary 当成固定 Chrome 的替代品。

## App 接入规则

在 app 代码里必须做能力检测和 fallback：

```js
const supportsHtmlInCanvas =
  typeof HTMLCanvasElement.prototype.requestPaint === "function" &&
  typeof CanvasRenderingContext2D.prototype.drawElementImage === "function";

if (!supportsHtmlInCanvas) {
  // fallback: normal DOM, SVG, plain Canvas, or static image
}
```

适合用它做：

- 本地 demo
- 视觉实验
- Canvas / WebGL / WebGPU 方向验证
- 技术文章截图
- 给开发者演示未来能力

不适合用它做：

- 线上生产功能
- 公众号最终排版
- 普通用户必须打开的页面
- 登录态平台操作
- 需要跨浏览器兼容的 app 核心能力

## 验收标准

打开烟测页后，至少确认：

- `canvas.requestPaint` 显示 `function`
- `CanvasRenderingContext2D.drawElementImage` 显示 `function`
- Canvas 区域能看到被绘制进去的 DOM 卡片

也可以直接跑：

```powershell
& 'C:\html\tools\verify-html-in-canvas.ps1'
```

通过时应看到：

```text
ok                        : True
browserVersion            : Chrome/150.0.7850.0
requestPaint              : function
drawElementImage          : function
captureElementImage       : function
texElementImage2D         : function
copyElementImageToTexture : function
```

如果显示 `undefined` 或空白，说明没有进入专用 Canary + flag 环境。
