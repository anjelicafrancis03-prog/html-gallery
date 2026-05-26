from PIL import Image, ImageDraw, ImageFont

OUT = r"C:\html\articles\wechat-automation-tools\assets"
FONT = r"C:\Windows\Fonts\msyh.ttc"
BOLD = r"C:\Windows\Fonts\msyhbd.ttc"


def f(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def wrap(draw, text, font, max_width):
    lines = []
    current = ""
    for ch in text:
        trial = current + ch
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
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
d.text((70, 38), "WECHAT AUTOMATION / TOOL RANKING", font=f(24, True), fill="#eaf6f2")
d.text((70, 158), "公众号自动化工具怎么选", font=f(58, True), fill="#182226")
text(d, (72, 238), "固定 Chrome 登录态是核心约束。工具排序看能不能接管真实浏览器、能不能长期脚本化、能不能留下验收证据。", f(26), "#4d5a60", 1040, 12)

cards = [
    ("主流程", "Playwright connectOverCDP", "接固定 Chrome 9223，适合后台、发表记录、公开页验收、截图和 DOM 检查。", "#0f6f68"),
    ("快速确认", "OpenCLI", "打开快、看 state 快，适合临时检查，不适合复杂批处理。", "#bf6b2f"),
    ("接管当前页", "CDP Bridge MCP", "桥在线时可执行 JS 和截图，适合交互探索。", "#295f92"),
    ("排障", "raw CDP", "最底层、最直接，但不适合日常主流程。", "#795548"),
    ("探索", "playwright-cli", "能截公开页，但会新开浏览器，不用于后台登录态。", "#6d5d9b"),
]

x0, y0 = 70, 348
for i, (tag, name, body, color) in enumerate(cards):
    y = y0 + i * 96
    rounded(d, (x0, y, 1330, y + 78), 14, "#fffdf8", "#d8d0c2")
    rounded(d, (96, y + 18, 230, y + 60), 21, color)
    d.text((118, y + 26), tag, font=f(19, True), fill="#ffffff")
    d.text((260, y + 17), name, font=f(27, True), fill="#182226")
    text(d, (660, y + 17), body, f(21), "#5b686f", 600, 6)

d.text((70, 840), "结论：日常主流程只认 Playwright connectOverCDP；其他工具按场景降级使用。", font=f(24, True), fill="#bf6b2f")
img.save(f"{OUT}\\tool-ranking.png")
