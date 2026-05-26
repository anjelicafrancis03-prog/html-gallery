const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const publishDir = __dirname;
const indexPath = path.join(root, 'index.html');
const outPath = path.join(publishDir, 'anysearch-comparison-publish.html');
const coverPath = path.join(publishDir, 'wechat-cover.png');

fs.mkdirSync(publishDir, { recursive: true });

const html = fs.readFileSync(indexPath, 'utf8');
const title = (html.match(/<title>([\s\S]*?)<\/title>/i) || [])[1] || 'AnySearch / Tavily / Brave 实测';
const description = (html.match(/<meta\s+name=["']description["']\s+content=["']([^"']*)["']/i) || [])[1] || '';
const body = (html.match(/<body[^>]*>([\s\S]*?)<\/body>/i) || [])[1] || html;
const main = (body.match(/<main[^>]*>([\s\S]*?)<\/main>/i) || [])[1] || body;
const header = (body.match(/<header[^>]*class=["']hero["'][^>]*>([\s\S]*?)<\/header>/i) || [])[1] || '';
const heroText = header
  .replace(/<aside[\s\S]*?<\/aside>/gi, '')
  .replace(/<div class=["']meta["'][\s\S]*?<\/div>/gi, '');

function absAsset(p) {
  if (/^(https?:|file:|data:)/i.test(p)) return p;
  return path.join(root, p.replace(/\//g, path.sep));
}

function clean(chunk) {
  return chunk
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<nav[\s\S]*?<\/nav>/gi, '')
    .replace(/\sclass=["'][^"']*["']/gi, '')
    .replace(/\sid=["'][^"']*["']/gi, '')
    .replace(/\saria-[a-z-]+=["'][^"']*["']/gi, '')
    .replace(/<div([^>]*)>/gi, '<section$1>')
    .replace(/<\/div>/gi, '</section>')
    .replace(/<article([^>]*)>/gi, '<section$1>')
    .replace(/<\/article>/gi, '</section>')
    .replace(/<img([^>]+)src=["']([^"']+)["']([^>]*)>/gi, (_, a, src, b) => {
      const full = absAsset(src);
      return `<img${a}src="${full}"${b} style="display:block;width:100%;height:auto;object-fit:contain;margin:18px auto;border:1px solid #ddd6c9;border-radius:4px;">`;
    });
}

const article = clean(`${heroText}${main}`);
const css = `
body{margin:0;background:#fffdf8;color:#182226;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",Arial,sans-serif;}
section{box-sizing:border-box;max-width:760px;margin:0 auto 22px;padding:0 4px;}
h1{margin:0 0 22px;font-size:32px;line-height:1.18;font-weight:800;color:#182226;}
h2{margin:34px 0 14px;font-size:23px;line-height:1.35;font-weight:800;color:#0f6f68;}
h3{margin:24px 0 10px;font-size:18px;line-height:1.45;font-weight:800;color:#182226;}
p{margin:0 0 16px;font-size:16px;line-height:1.86;color:#2f3a40;}
strong,b{font-weight:800;color:#182226;}
figure{max-width:760px;margin:24px auto;padding:0;}
figcaption{margin:8px 0 0;font-size:13px;line-height:1.7;color:#657078;text-align:center;}
table{width:100%;border-collapse:collapse;margin:18px 0;font-size:14px;line-height:1.65;background:#fff;}
th,td{border:1px solid #ddd6c9;padding:10px 8px;vertical-align:top;text-align:left;}
th{background:#eef5f3;color:#0f6f68;font-weight:800;}
pre{white-space:pre-wrap;word-break:break-word;margin:16px 0;padding:14px;border-radius:4px;background:#152225;color:#f4f1e8;font-size:13px;line-height:1.7;}
code{font-family:Consolas,"SFMono-Regular",monospace;}
img{max-width:100%;height:auto;object-fit:contain;}
.wrap{max-width:760px;margin:0 auto;padding:26px 16px 44px;background:#fffdf8;}
`;

const publishHtml = `<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${title}</title>
  <meta name="description" content="${description}">
  <style>${css}</style>
</head>
<body>
  <section class="wrap" id="wechat-output">${article}</section>
</body>
</html>`;

fs.writeFileSync(outPath, publishHtml, 'utf8');
console.log(JSON.stringify({ outPath, coverPath }, null, 2));
