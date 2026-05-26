from PIL import Image, ImageDraw, ImageFont

OUT = r"C:\html\articles\wechatdownload-mcp-tool\assets"
FONT = r"C:\Windows\Fonts\msyh.ttc"
BOLD = r"C:\Windows\Fonts\msyhbd.ttc"


def f(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def wrap(draw, text, font, max_width):
    lines, cur = [], ""
    for ch in text:
        trial = cur + ch
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def text(draw, xy, content, font, fill, max_width, gap=8):
    x, y = xy
    for line in wrap(draw, content, font, max_width):
        draw.text((x, y), line, font=font, fill=fill)
        y += font.size + gap
    return y


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


img = Image.new("RGB", (1400, 900), "#f7f4ec")
d = ImageDraw.Draw(img)
d.rectangle((0, 0, 1400, 112), fill="#0f6f68")
d.text((70, 38), "WECHATDOWNLOAD MCP / BATCH ARCHIVER", font=f(24, True), fill="#eaf6f2")
d.text((70, 158), "公众号文章批量下载工具", font=f(58, True), fill="#182226")
text(d, (72, 240), "Agent 通过 MCP JSON-RPC 把真实 mp.weixin.qq.com/s/... 链接交给本地工具，自动落盘 Markdown、HTML、MHTML、DOCX、PDF 和图片。", f(27), "#4d5a60", 1120, 12)

stats = [
    ("545", "触发链接"),
    ("545", "触发成功"),
    ("501", "有效 Markdown 正文"),
    ("6", "落盘格式"),
]
x = 70
for value, label in stats:
    rounded(d, (x, 380, x + 290, 560), 18, "#fffdf8", "#d8d0c2")
    d.text((x + 34, 414), value, font=f(58, True), fill="#0f6f68")
    d.text((x + 36, 500), label, font=f(24, True), fill="#59666d")
    x += 320

steps = [
    "索引页提取真实公众号链接",
    "MCP tools/list 确认工具能力",
    "单篇 smoke test",
    "批量触发下载",
    "扫描本地正文验收",
]
x, y = 70, 640
for i, step in enumerate(steps, 1):
    rounded(d, (x, y, x + 244, y + 92), 14, "#edf5f2", "#bed9d3")
    d.text((x + 18, y + 18), f"{i:02d}", font=f(26, True), fill="#bf6b2f")
    text(d, (x + 68, y + 18), step, f(21, True), "#182226", 150, 6)
    x += 258

d.text((70, 835), "边界：索引页只提供链接，正文必须走 mp.weixin.qq.com 原文链接。", font=f(24, True), fill="#bf6b2f")
img.save(f"{OUT}\\hero-tool-summary.png")
