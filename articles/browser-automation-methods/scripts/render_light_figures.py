from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


OUT = Path(r"F:\codex\browser-method-comparison-html\assets")
W, H = 1536, 1024


def font(size, bold=False, family=None):
    path = r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc"
    return ImageFont.truetype(path, size=size)


def draw_round(draw, xy, fill, outline, radius=24, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def center_text(draw, y, text, fnt, fill, box=(0, W), anchor="mm"):
    x = (box[0] + box[1]) / 2
    draw.text((x, y), text, font=fnt, fill=fill, anchor=anchor)


def wrapped(draw, text, fnt, fill, left, top, width, line_gap=8, max_lines=3, align="left"):
    words = list(text)
    lines = []
    line = ""
    for ch in words:
        test = line + ch
        if draw.textlength(test, font=fnt) <= width or not line:
            line = test
        else:
            lines.append(line)
            line = ch
    if line:
        lines.append(line)
    lines = lines[:max_lines]
    y = top
    for ln in lines:
        if align == "center":
            x = left + width / 2
            draw.text((x, y), ln, font=fnt, fill=fill, anchor="ma")
        else:
            draw.text((left, y), ln, font=fnt, fill=fill)
        y += fnt.size + line_gap


def base_canvas():
    img = Image.new("RGB", (W, H), "#fbf6ec")
    draw = ImageDraw.Draw(img)
    draw_round(draw, (42, 42, W - 42, H - 42), "#fffdf8", "#d8c7ad", radius=26, width=2)
    return img, draw


def rank_overview():
    img, draw = base_canvas()
    draw.text((W / 2, 120), "浏览器方式总评定", font=font(62, True), fill="#20251f", anchor="mm")
    draw.text((W / 2, 176), "先分清：谁做生产主力，谁做会话接管，谁只适合探索或降级", font=font(25), fill="#6d6252", anchor="mm")
    rows = [
        ("1", "Playwright CDP", "生产主力", "9.2", "长期脚本、定时任务、字段抽取最稳", "#f3dfbd"),
        ("2", "CDP Bridge MCP", "真实会话", "8.5", "接管已登录浏览器，读当前标签页和执行 JS", "#e7f2eb"),
        ("3", "OpenCLI", "快速操作", "8.0", "打开、点击、state、extract，适合快速验证", "#fff9ee"),
        ("4", "playwright-cli", "探索固化", "7.7", "边看页面边调选择器，最后沉淀脚本", "#fff9ee"),
        ("5", "raw CDP", "底层急救", "6.8", "排查 9223、DOM、请求，维护成本高", "#fff9ee"),
        ("6", "Codex Chrome 插件", "交互辅助", "6.5", "辅助浏览器任务，不承担主爬虫线", "#fff9ee"),
        ("7", "HTTP / Scrapy", "降级路线", "4.0", "静态页面可用，动态登录社媒不占优", "#fff9ee"),
    ]
    y = 232
    for num, name, tag, score, desc, fill in rows:
        draw_round(draw, (96, y, 1440, y + 82), fill, "#d8c7ad", radius=14, width=2)
        draw.text((126, y + 38), num, font=font(48, True), fill="#8f5e2c", anchor="mm")
        draw.text((230, y + 25), name, font=font(30, True), fill="#20251f")
        draw.text((590, y + 29), tag, font=font(22), fill="#2f7f6c")
        draw.text((790, y + 25), score, font=font(30, True), fill="#8f5e2c", anchor="mm")
        wrapped(draw, desc, font(22), "#6d6252", 920, y + 18, 450, max_lines=2)
        y += 92
    draw.text((W / 2, 905), "最终保留：Playwright 做生产线；CDP Bridge / OpenCLI / playwright-cli 做探索、接管和调试。",
              font=font(24, True), fill="#20251f", anchor="mm")
    img.save(OUT / "rank-overview-light.png")


def workflow_layers():
    img, draw = base_canvas()
    draw.text((W / 2, 120), "分层落地路线", font=font(62, True), fill="#20251f", anchor="mm")
    draw.text((W / 2, 176), "看现场、试动作、固化路径、批量生产，四层分工", font=font(25), fill="#6d6252", anchor="mm")
    steps = [
        ("01", "CDP Bridge MCP", "读真实浏览器现场", "复用已登录 Chrome，读取标签页、正文、Cookie，执行轻量 JS", "#fff9ee"),
        ("02", "OpenCLI", "快速完成页面操作", "open / state / click / extract，适合临时搜索、验证、排障", "#eef6f0"),
        ("03", "playwright-cli", "探索并固化路径", "处理按钮、iframe、下载、滚动，沉淀稳定选择器", "#fff9ee"),
        ("04", "Playwright", "最终批量生产", "写成 Python 脚本，接 CSV / SQLite / Parquet / 定时任务", "#eef6f0"),
    ]
    y = 242
    for idx, name, tag, desc, fill in steps:
        draw_round(draw, (210, y, 1326, y + 126), fill, "#d8c7ad", radius=18, width=2)
        draw_round(draw, (238, y + 25, 326, y + 101), "#8f5e2c", None, radius=14, width=0)
        draw.text((282, y + 63), idx, font=font(34, True), fill="#fffdf8", anchor="mm")
        draw.text((370, y + 26), name, font=font(34, True), fill="#20251f")
        draw.text((370, y + 66), tag, font=font(22), fill="#2f7f6c")
        wrapped(draw, desc, font(22), "#6d6252", 750, y + 34, 460, max_lines=3)
        y += 156
    draw.text((W / 2, 905), "AI 负责探索，Playwright 负责长期运行。", font=font(30, True), fill="#8f5e2c", anchor="mm")
    img.save(OUT / "workflow-layers-light.png")


def decision_map():
    img, draw = base_canvas()
    draw.text((W / 2, 120), "场景选型", font=font(62, True), fill="#20251f", anchor="mm")
    draw.text((W / 2, 176), "按你的任务类型直接选，不再纠结“哪个工具最强”", font=font(25), fill="#6d6252", anchor="mm")
    cols = [
        ("日常稳定抓取", "每天 / 每周跑批，导出结构化字段", "Playwright", "CSV / SQLite / Parquet"),
        ("真实浏览器接管", "已登录并打开页面，需要模型读取现场", "CDP Bridge MCP", "OpenCLI 辅助操作"),
        ("探索式调试", "按钮、iframe、滚动、下载路径不稳定", "playwright-cli", "最终转 Playwright"),
    ]
    x = 104
    for title, desc, tool, tail in cols:
        draw_round(draw, (x, 244, x + 408, 784), "#fff9ee", "#d8c7ad", radius=20, width=2)
        draw_round(draw, (x + 38, 290, x + 134, 386), "#edf5ef", None, radius=48, width=0)
        draw.text((x + 86, 338), "✓", font=font(54, True), fill="#2f7f6c", anchor="mm")
        draw.text((x + 204, 426), title, font=font(34, True), fill="#20251f", anchor="mm")
        wrapped(draw, desc, font(22), "#6d6252", x + 46, 500, 316, max_lines=2, align="center")
        draw.line((x + 80, 626, x + 328, 626), fill="#8f5e2c", width=3)
        draw.text((x + 204, 674), "推荐主工具", font=font(18), fill="#8f5e2c", anchor="mm")
        draw.text((x + 204, 730), tool, font=font(28, True), fill="#20251f", anchor="mm")
        draw.text((x + 204, 778), tail, font=font(22), fill="#2f7f6c", anchor="mm")
        x += 462
    draw.text((W / 2, 905), "判断顺序：先看是否要长期批处理，再看是否必须复用真实登录态，最后才看探索效率。",
              font=font(22), fill="#20251f", anchor="mm")
    img.save(OUT / "decision-map-light.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    rank_overview()
    workflow_layers()
    decision_map()
