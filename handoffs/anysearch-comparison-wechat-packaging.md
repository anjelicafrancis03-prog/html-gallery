# AnySearch 对比文章公众号封装交接

源文章：

```text
C:\html\articles\anysearch-comparison\index.html
```

公众号封装注意事项：

```text
C:\html\articles\anysearch-comparison\publish\wechat-packaging-notes.md
```

核心要求：

1. 不要直接粘整页 HTML。
2. 改成单列公众号长文。
3. 三张信息图使用 PNG，单列展示，不横排、不裁剪。
4. 网页表格改成工具卡片。
5. 关键 CSS 内联到元素 `style=""`。
6. 删除 JS、目录跳转、复杂 grid/flex、动画。
7. 保留 agent 口令文本块，方便复制。
8. 公众号后台操作必须先验证固定 Chrome。

正文图：

```text
C:\html\articles\anysearch-comparison\assets\card-01-overview.png
C:\html\articles\anysearch-comparison\assets\card-02-samples.png
C:\html\articles\anysearch-comparison\assets\card-03-how-to-use.png
```

建议封面：

```text
标题：AnySearch 实测
副标题：技术检索该怎么用
比例：900x383 或 1200x510
目录：C:\html\articles\anysearch-comparison\imgs\
```

固定 Chrome 验证：

```powershell
& 'F:\codex\tools\verify-codex-fixed-chrome.ps1' -RestartIfMissingExtension
```
