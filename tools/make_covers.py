from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import textwrap

ROOT = Path(r"C:\html\articles")
W, H = 1200, 510

ITEMS = [
    {
        "slug": "html-skills-comparison",
        "title": "四个 HTML Skill 横向对比：谁负责审美，谁负责文章，谁负责交付",
        "subtitle": "HTML 专门文章 · 工序化工作流",
        "src": ROOT / "html-skills-comparison" / "assets" / "html-skills-hero-v3.png",
        "out": ROOT / "html-skills-comparison" / "imgs" / "cover.png",
        "accent": (210, 172, 98),
        "bg": (19, 20, 17),
        "badge": "HTML Skill Stack",
        "chips": ["设计总监", "主笔", "图解", "交付"],
    },
    {
        "slug": "browser-automation-methods",
        "title": "真实浏览器爬取方案重新评定",
        "subtitle": "固定 Chrome · 登录态 · 方案选型",
        "src": ROOT / "browser-automation-methods" / "assets" / "rank-overview-light.png",
        "out": ROOT / "browser-automation-methods" / "imgs" / "cover.png",
        "accent": (79, 177, 155),
        "bg": (16, 23, 23),
        "badge": "Browser Automation",
        "chips": ["Playwright", "OpenCLI", "CDP Bridge", "Playwright CLI"],
    },
    {
        "slug": "codex-feishu-bridge-control-plane",
        "title": "我把 Codex 接到飞书后，最大的变化不是“手机能聊天”",
        "subtitle": "飞书入口 · 同线程 · 长期状态",
        "src": ROOT / "codex-feishu-bridge-control-plane" / "assets" / "workflow-ai-thread-control.png",
        "out": ROOT / "codex-feishu-bridge-control-plane" / "imgs" / "cover.png",
        "accent": (92, 145, 255),
        "bg": (12, 17, 26),
        "badge": "Codex × Feishu",
        "chips": ["接线", "同线程", "状态", "边界"],
    },
]

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\simkai.ttf",
]
BODY_CANDIDATES = [
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
]


def load_font(cands, size):
    for p in cands:
        path = Path(p)
        if path.exists():
            try:
                return ImageFont.truetype(str(path), size=size)
            except Exception:
                pass
    return ImageFont.load_default()


FONT_TITLE = load_font(FONT_CANDIDATES, 54)
FONT_SUB = load_font(BODY_CANDIDATES, 24)
FONT_BADGE = load_font(BODY_CANDIDATES, 18)
FONT_CHIP = load_font(BODY_CANDIDATES, 18)
FONT_FOOT = load_font(BODY_CANDIDATES, 16)


def fit_bg(src: Image.Image) -> Image.Image:
    return ImageOps.fit(src, (W, H), method=Image.Resampling.LANCZOS, centering=(0.5, 0.42))


def add_gradient_overlay(base: Image.Image, bg_color):
    overlay = Image.new("RGBA", (W, H), bg_color + (0,))
    od = ImageDraw.Draw(overlay)
    for x in range(W):
        alpha = int(190 * (1 - min(1, x / (W * 0.80))))
        od.line([(x, 0), (x, H)], fill=bg_color + (alpha,))
    return Image.alpha_composite(base, overlay)


def make_cover(item):
    src = Image.open(item["src"]).convert("RGB")
    bg = fit_bg(src).filter(ImageFilter.GaussianBlur(1.0)).convert("RGBA")
    base = add_gradient_overlay(bg, item["bg"])

    # right-side visual card
    card_w, card_h = 406, 300
    card_x, card_y = 740, 104
    thumb = ImageOps.fit(src, (card_w, card_h), method=Image.Resampling.LANCZOS, centering=(0.5, 0.42)).convert("RGBA")

    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh = ImageDraw.Draw(shadow)
    sh.rounded_rectangle([card_x + 10, card_y + 12, card_x + card_w + 10, card_y + card_h + 12], radius=28, fill=(0, 0, 0, 82))
    base = Image.alpha_composite(base, shadow)

    mask = Image.new("L", (card_w, card_h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, card_w - 1, card_h - 1], radius=28, fill=255)
    card = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    card.paste(thumb, (card_x, card_y), mask)
    base = Image.alpha_composite(base, card)

    draw = ImageDraw.Draw(base)

    pad_x, pad_y = 72, 68
    badge_box = [pad_x, pad_y, pad_x + 330, pad_y + 40]
    draw.rounded_rectangle(badge_box, radius=20, fill=item["accent"] + (220,))
    draw.text((pad_x + 18, pad_y + 8), item["badge"], font=FONT_BADGE, fill=(255, 255, 255))

    lines = textwrap.wrap(item["title"], width=14 if len(item["title"]) > 18 else 18)
    y = pad_y + 72
    for line in lines[:4]:
        draw.text((pad_x, y), line, font=FONT_TITLE, fill=(255, 255, 255))
        bbox = draw.textbbox((pad_x, y), line, font=FONT_TITLE)
        y = bbox[3] + 10

    draw.text((pad_x, y + 2), item["subtitle"], font=FONT_SUB, fill=(235, 235, 235))

    chip_x = pad_x
    chip_y = H - 88
    for chip in item["chips"]:
        bbox = draw.textbbox((0, 0), chip, font=FONT_CHIP)
        cw = bbox[2] - bbox[0] + 28
        ch = bbox[3] - bbox[1] + 16
        draw.rounded_rectangle([chip_x, chip_y, chip_x + cw, chip_y + ch], radius=18, fill=(255, 255, 255, 224))
        draw.text((chip_x + 14, chip_y + 8), chip, font=FONT_CHIP, fill=(26, 34, 48))
        chip_x += cw + 10

    draw.text((1048, H - 33), "C:\\html cover", font=FONT_FOOT, fill=(245, 245, 245))
    item["out"].parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(item["out"], quality=96)
    return item["out"]


def main():
    for item in ITEMS:
        out = make_cover(item)
        print(out)


if __name__ == "__main__":
    main()
