from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"C:\html\articles\anysearch-comparison\assets"
FONT = r"C:\Windows\Fonts\msyh.ttc"
BOLD = r"C:\Windows\Fonts\msyhbd.ttc"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size=size)


def wrap(draw, text, fnt, max_width):
    lines = []
    for paragraph in text.split("\n"):
        current = ""
        for char in paragraph:
            trial = current + char
            if draw.textbbox((0, 0), trial, font=fnt)[2] <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = char
        if current:
            lines.append(current)
    return lines


def draw_text(draw, xy, text, fnt, fill, max_width, line_gap=10):
    x, y = xy
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def card_base(title, subtitle, filename):
    img = Image.new("RGB", (1400, 900), "#f7f4ec")
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 1400, 110), fill="#0f6f68")
    draw.text((70, 38), "SEARCH BENCHMARK / LOCAL TEST", font=font(22, True), fill="#eaf6f2")
    draw.text((70, 154), title, font=font(56, True), fill="#182226")
    draw_text(draw, (72, 232), subtitle, font(26), "#4c5960", 980, 12)
    return img, draw


def overview():
    img, draw = card_base(
        "AnySearch / Tavily / Brave 怎么分工",
        "结论不是谁替代谁，而是把“找出处、交叉验证、解释总结”拆开。",
        "card-01-overview.png",
    )
    headers = ["工具", "强项", "短板", "位置"]
    rows = [
        ["AnySearch", "README / docs / benchmark / 参数表", "重名项目需加限定词", "主搜索源"],
        ["Tavily", "结构化结果 / 第二来源 / RAG", "可能被同名项目带偏", "交叉验证"],
        ["Brave", "通用网页搜索", "本机缺 key，网页版 429", "待接入"],
        ["DeepSeek", "解释和总结", "不是实时搜索", "理解层"],
    ]
    x0, y0 = 70, 360
    widths = [190, 430, 390, 230]
    heights = [64] + [92] * len(rows)
    colors = ["#e9f4f1", "#fffdf8"]
    x = x0
    for i, h in enumerate(headers):
        rounded(draw, (x, y0, x + widths[i], y0 + heights[0]), 0, "#dcece8", "#c9d9d4")
        draw.text((x + 18, y0 + 18), h, font=font(24, True), fill="#0f4f4a")
        x += widths[i]
    y = y0 + heights[0]
    for ridx, row in enumerate(rows):
        x = x0
        for cidx, cell in enumerate(row):
            rounded(draw, (x, y, x + widths[cidx], y + heights[ridx + 1]), 0, colors[ridx % 2], "#d8d0c2")
            f = font(22, cidx == 0)
            fill = "#182226" if cidx != 3 else "#0f6f68"
            draw_text(draw, (x + 18, y + 18), cell, f, fill, widths[cidx] - 36, 6)
            x += widths[cidx]
        y += heights[ridx + 1]
    draw.text((70, 828), "建议口令：用 anysearch + tavily 对比搜索：<主题>", font=font(24, True), fill="#bf6b2f")
    img.save(f"{OUT_DIR}\\card-01-overview.png")


def samples():
    img, draw = card_base(
        "样本证据：AnySearch 胜在命中原始出处",
        "这轮测试重点看原始 URL、项目是否命中、关键数字是否直接出现。",
        "card-02-samples.png",
    )
    items = [
        ("CodeGraph benchmark", "AnySearch 命中 colbymchenry/codegraph README，并带出 52 calls / 1m37s 到 3 calls / 17s。"),
        ("CVE-2024-3094", "AnySearch 和 Tavily 都能找到 OpenSSF、NVD、JFrog 等安全来源，适合交叉验证。"),
        ("ngrok free domain", "Tavily 更容易补到 ngrok 官方博客和 docs，适合做第二搜索源。"),
        ("GPT Image 2 docs", "两者都能命中 OpenAI 文档，最终应回到官方 docs/API reference 确认。"),
    ]
    y = 350
    for i, (title, body) in enumerate(items):
        rounded(draw, (70, y, 1330, y + 112), 14, "#fffdf8", "#d8d0c2")
        draw.ellipse((96, y + 34, 140, y + 78), fill="#0f6f68" if i == 0 else "#bf6b2f")
        draw.text((160, y + 22), title, font=font(28, True), fill="#182226")
        draw_text(draw, (160, y + 62), body, font(22), "#59666d", 1060, 7)
        y += 126
    draw.text((70, 828), "判断标准：先看 URL 是否命中原始出处，再看摘要是否带出关键证据。", font=font(24, True), fill="#0f6f68")
    img.save(f"{OUT_DIR}\\card-02-samples.png")


def workflow():
    img, draw = card_base(
        "以后怎么用：三步固定流程",
        "把搜索链路拆开，避免让 Chat API 假装自己会搜索。",
        "card-03-how-to-use.png",
    )
    steps = [
        ("01", "AnySearch 找出处", "优先 GitHub README、官方文档、参数表、CVE、厂商公告。"),
        ("02", "Tavily 做交叉验证", "检查结构化结果是否支持同一结论，尤其核对 URL。"),
        ("03", "模型负责解释", "只基于已拿到的证据做总结、判断、写作和发布改写。"),
    ]
    x = 70
    for num, title, body in steps:
        rounded(draw, (x, 350, x + 386, 690), 18, "#fffdf8", "#d8d0c2")
        draw.text((x + 32, 386), num, font=font(48, True), fill="#bf6b2f")
        draw.text((x + 32, 462), title, font=font(30, True), fill="#182226")
        draw_text(draw, (x + 32, 520), body, font(23), "#59666d", 312, 8)
        x += 424
    rounded(draw, (70, 750, 1330, 832), 12, "#142326", None)
    draw.text((100, 775), "口令：用 anysearch + tavily 对比搜索：<主题>", font=font(27, True), fill="#f5f1e8")
    img.save(f"{OUT_DIR}\\card-03-how-to-use.png")


if __name__ == "__main__":
    overview()
    samples()
    workflow()
