from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap

OUT = Path(__file__).resolve().parent
FONT = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


def multiline(draw, text, xy, fnt, fill, width_chars, line_gap=10):
    x, y = xy
    lines = []
    for part in text.split("\n"):
        lines.extend(textwrap.wrap(part, width=width_chars) or [""])
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def workflow():
    w, h = 1600, 1050
    img = Image.new("RGB", (w, h), "#f7f3ea")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, w, 170), fill="#1f5f58")
    d.text((70, 52), "HTML 文章生产线", font=font(52, True), fill="#fffaf0")
    d.text((72, 116), "从材料到母版，再到平台发布包，所有环节都可验收、可交接、可复用", font=font(25), fill="#dfeee8")

    steps = [
        ("01", "收集材料", "主题、报告、截图、数据、参考文章"),
        ("02", "生成母版", "C:\\html\\articles\\<slug>\\index.html"),
        ("03", "补图验收", "真实截图 / 信息图 / image2，localhost 检查"),
        ("04", "平台封装", "公众号、飞书、知乎分别降级转换"),
        ("05", "交接记忆", "README、handoff、口令和踩坑经验沉淀"),
    ]
    x0, y0 = 70, 260
    card_w, card_h, gap = 280, 470, 22
    colors = ["#fffdf7", "#eef5f1", "#fff8ed", "#eef2fa", "#f9f0ef"]
    for i, (num, title, desc) in enumerate(steps):
        x = x0 + i * (card_w + gap)
        rounded(d, (x, y0, x + card_w, y0 + card_h), 22, colors[i], "#d9ccba", 3)
        d.text((x + 26, y0 + 28), num, font=font(42, True), fill="#b35b34")
        d.text((x + 26, y0 + 105), title, font=font(34, True), fill="#172429")
        multiline(d, desc, (x + 26, y0 + 170), font(25), "#4d5b61", 12, 14)
        if i < len(steps) - 1:
            ax = x + card_w + 7
            ay = y0 + 230
            d.line((ax, ay, ax + gap - 6, ay), fill="#1f5f58", width=5)
            d.polygon([(ax + gap - 6, ay), (ax + gap - 20, ay - 10), (ax + gap - 20, ay + 10)], fill="#1f5f58")

    d.text((74, 830), "验收线：HTTP 200 / 无乱码 / 图片全加载 / 桌面与手机无横向溢出 / 关键区域截图检查", font=font(30, True), fill="#1f5f58")
    d.text((74, 885), "一句话：HTML 是母版，localhost 是验收线，publish 是平台版，C:\\html 是总仓库。", font=font(29), fill="#2b3b40")
    img.save(OUT / "workflow-pipeline.png", quality=95)


def directory():
    w, h = 1500, 1000
    img = Image.new("RGB", (w, h), "#fbf8f0")
    d = ImageDraw.Draw(img)
    d.text((70, 60), "C:\\html 成品目录规范", font=font(54, True), fill="#172429")
    d.text((72, 128), "每篇文章独立目录，图片、发布包、封面和验收记录都跟着文章走", font=font(27), fill="#637078")

    tree = [
        ("C:\\html", "所有线程共享的 HTML 总仓库"),
        ("articles\\<slug>\\index.html", "HTML 母版，完整排版和视觉结构"),
        ("articles\\<slug>\\assets\\", "正文图、截图、信息图、视频帧"),
        ("articles\\<slug>\\publish\\", "公众号、飞书、知乎等平台版本"),
        ("articles\\<slug>\\imgs\\", "封面、缩略图、平台裁剪尺寸"),
        ("README.md", "登记当前成品和交接规则"),
    ]
    y = 245
    for i, (path, note) in enumerate(tree):
        fill = "#ffffff" if i % 2 == 0 else "#f1f6f2"
        rounded(d, (90, y, 1410, y + 92), 14, fill, "#d7cdbc", 2)
        d.text((125, y + 25), path, font=font(29, True), fill="#1f5f58")
        d.text((650, y + 27), note, font=font(25), fill="#3f4d53")
        y += 112

    rounded(d, (90, 885, 1410, 945), 12, "#1f5f58", None)
    d.text((125, 901), "规则：不要混用全局 assets；不要只给 file://；新增成品必须更新 README。", font=font(25, True), fill="#fffaf0")
    img.save(OUT / "directory-standard.png", quality=95)


def platform():
    w, h = 1600, 1050
    img = Image.new("RGB", (w, h), "#f6f4ec")
    d = ImageDraw.Draw(img)
    d.text((70, 55), "平台封装决策图", font=font(56, True), fill="#172429")
    d.text((72, 125), "同一篇 HTML 母版，按平台能力降级，不追求所有平台 100% 原样", font=font(27), fill="#66727b")

    lanes = [
        ("公众号", "#eef7f1", "CSS 内联\n表格改卡片\n复杂图转 PNG\n封面单独制作"),
        ("飞书文档", "#eef2fb", "结构优先\n图表转表格\n截图前置\n视频做附件"),
        ("知乎", "#fff7e8", "长文逻辑优先\n图片可保留\n复杂排版会损失\n公式单独处理"),
        ("小红书 / 社媒", "#faeeee", "文章拆卡片\n高 DPI PNG\n标题封面重做\n移动端先验收"),
    ]
    x0, y0 = 70, 245
    card_w, card_h, gap = 350, 560, 28
    for i, (name, bg, bullets) in enumerate(lanes):
        x = x0 + i * (card_w + gap)
        rounded(d, (x, y0, x + card_w, y0 + card_h), 24, bg, "#d6ccbd", 3)
        d.text((x + 32, y0 + 36), name, font=font(38, True), fill="#b35b34")
        yy = y0 + 130
        for line in bullets.split("\n"):
            d.ellipse((x + 34, yy + 10, x + 48, yy + 24), fill="#1f5f58")
            d.text((x + 62, yy), line, font=font(27), fill="#26343a")
            yy += 85

    d.line((90, 880, 1510, 880), fill="#1f5f58", width=4)
    d.text((95, 910), "判断标准：平台能承受什么，就交付什么。HTML 母版负责完整表达，publish 版负责稳定发布。", font=font(29, True), fill="#1f5f58")
    img.save(OUT / "platform-packaging.png", quality=95)


if __name__ == "__main__":
    workflow()
    directory()
    platform()
    print("generated infographics in", OUT)
