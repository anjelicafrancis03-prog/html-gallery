const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const outDir = __dirname;
const assetDir = path.join(outDir, 'assets');
fs.mkdirSync(assetDir, { recursive: true });

const assets = [
  'card-01-overview.png',
  'card-02-samples.png',
  'card-03-how-to-use.png',
];

for (const name of assets) {
  fs.copyFileSync(path.join(root, 'assets', name), path.join(assetDir, name));
}

const title = 'AnySearch / Tavily / Brave 实测：以后技术检索该怎么用';
const summary = '基于本地搜索样本的 AnySearch、Tavily、Brave、DeepSeek 对比测评：技术检索、原始出处、结构化结果和使用工作流。';

const S = {
  wrap: 'max-width:760px;margin:0 auto;padding:24px 12px 44px;background:#fffdf8;color:#182226;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",Arial,sans-serif;',
  h1: 'margin:0 0 18px;font-size:28px;line-height:1.25;font-weight:800;color:#182226;letter-spacing:0;',
  p: 'margin:0 0 16px;font-size:16px;line-height:1.86;color:#2f3a40;letter-spacing:0;',
  lead: 'margin:0 0 18px;padding:14px 16px;background:#eef5f3;border-left:5px solid #0f6f68;font-size:16px;line-height:1.86;color:#182226;font-weight:700;',
  h2: 'margin:34px 0 14px;font-size:22px;line-height:1.4;font-weight:800;color:#0f6f68;letter-spacing:0;',
  h3: 'margin:0 0 8px;font-size:18px;line-height:1.45;font-weight:800;color:#182226;',
  card: 'margin:14px 0;padding:16px;background:#ffffff;border:1px solid #ddd6c9;border-radius:6px;',
  tag: 'display:inline-block;margin:0 0 9px;padding:4px 8px;background:#f5efe5;color:#bf6b2f;border-radius:4px;font-size:13px;font-weight:800;',
  img: 'display:block;width:100%;height:auto;object-fit:contain;margin:18px auto;border:1px solid #ddd6c9;border-radius:4px;background:#fff;',
  caption: 'margin:-8px 0 20px;text-align:center;font-size:13px;line-height:1.7;color:#657078;',
  quote: 'margin:18px 0;padding:15px 16px;background:#f7f4ec;border:1px solid #ddd6c9;border-radius:6px;font-size:15px;line-height:1.8;color:#3d4a50;',
  prompt: 'margin:14px 0;padding:14px 16px;background:#f2f4f5;border:1px solid #d8dde0;border-radius:6px;font-size:15px;line-height:1.8;color:#182226;font-family:"Microsoft YaHei",Arial,sans-serif;white-space:pre-wrap;',
};

function p(text, style = S.p) {
  return `<p style="${style}">${text}</p>`;
}

function h2(text) {
  return `<h2 style="${S.h2}">${text}</h2>`;
}

function card(name, tag, strong, weak, place) {
  return `<section style="${S.card}">
    <span style="${S.tag}">${tag}</span>
    <h3 style="${S.h3}">${name}</h3>
    ${p(`<strong>强项：</strong>${strong}`)}
    ${p(`<strong>短板：</strong>${weak}`)}
    ${p(`<strong>建议位置：</strong>${place}`)}
  </section>`;
}

function img(name, caption) {
  return `<img src="assets/${name}" alt="${caption}" style="${S.img}">
  <p style="${S.caption}">${caption}</p>`;
}

const html = `<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${title}</title>
  <meta name="description" content="${summary}">
</head>
<body style="margin:0;background:#fffdf8;">
  <section id="wechat-output" style="${S.wrap}">
    <h1 style="${S.h1}">${title}</h1>
    ${p('结论先放前面：以后做技术检索，AnySearch 应该放在第一搜索源，Tavily 做第二搜索源和交叉验证，Brave 等 API key 接好后再进入主流程，DeepSeek 只负责解释和压缩，不负责找原始出处。', S.lead)}
    ${p('这篇不是抽象比较“谁更聪明”，而是按真实 Agent 工作流去看：找 GitHub README、官方文档、参数表、benchmark 数字、CVE 原始出处时，谁更容易把人带到可靠来源。')}

    ${img('card-01-overview.png', '总览图：四种工具在技术检索链路里的位置。')}

    ${h2('一、四种工具不要混着用')}
    ${p('搜索、验证、解释、写作是四件事。把它们混在一个模型回答里，结果往往是看起来顺滑，但出处不稳。更稳的做法，是给每个工具固定角色。')}
    ${card('AnySearch', '主搜索源', '更适合找 GitHub README、官方 docs、开源项目、benchmark、参数表和 URL extract。它的价值是把 Agent 带到原始页面。', '中文结果偶尔会混入低质量页面；遇到重名项目仍然要加 owner/repo、官方域名或精确 URL。', '技术检索第一搜索源。')}
    ${card('Tavily', '第二搜索源', '结构化 JSON 好处理，适合补充证据、网页摘要和 RAG 入口。', 'answer 看起来完整，但重名项目时会被带偏；必须看 URL 是否命中同一个对象。', '第二搜索源和交叉验证。')}
    ${card('Brave Search', '待接入源', '通用网页搜索生态完整，理论上适合补齐搜索结果。', '这次本机没有完整 API key，网页版又遇到 429，不能算严肃完整实测。', '等 BRAVE_SEARCH_API_KEY 接好后再进主流程。')}
    ${card('DeepSeek Chat API', '解释层', '适合解释搜索结果、压缩长文、总结差异、生成最终判断。', '不能访问实时网页，不应该被当成搜索引擎。', '搜索后的理解层，不放在找出处层。')}

    ${h2('二、关键样本：优势在“命中原始出处”')}
    ${img('card-02-samples.png', '样本图：CodeGraph、CVE、OpenAI GPT Image 2、ngrok 等查询的命中差异。')}
    ${p('<strong>CodeGraph benchmark：</strong>AnySearch 命中 `colbymchenry/codegraph` README，并带出关键表格；Tavily 则优先返回另一个同名项目，语义相关但对象偏了。')}
    ${p('<strong>CVE-2024-3094：</strong>AnySearch 命中 OpenSSF、JFrog、NVD 等安全出处；安全类查询不能只看 summary，要优先抓官方、安全机构和供应商公告。')}
    ${p('<strong>ngrok free static domain：</strong>Tavily 更容易补到官方博客和 docs，说明它适合作第二来源，尤其是产品功能类查询。')}
    ${p('<strong>OpenAI GPT Image 2 docs：</strong>两边都能命中 OpenAI 文档和 API reference，但涉及 OpenAI 产品，最终仍应回到官方文档确认。')}

    ${h2('三、以后直接按这个流程跑')}
    ${img('card-03-how-to-use.png', '流程图：给其他线程最容易执行的搜索口令和验证顺序。')}
    ${p('<strong>第一步：先用 AnySearch 找原始出处。</strong>目标是 README、官方 docs、GitHub、NVD、厂商公告和参数表，不是先要模型总结。')}
    ${p('<strong>第二步：再用 Tavily 做交叉验证。</strong>重点看结构化结果是否支持同一结论，URL 是否命中同一个项目或同一份文档。')}
    ${p('<strong>第三步：最后让模型解释。</strong>模型只处理已经拿到的证据：抽结论、比较差异、写文章、生成使用建议。')}

    ${h2('四、给其他 Agent 的口令')}
    <section style="${S.prompt}">用 anysearch + tavily 对比搜索：&lt;主题&gt;

要求：AnySearch 优先找 GitHub README / 官方 docs / 原始出处；Tavily 做第二搜索源；输出命中差异、关键 URL、结论和使用建议。</section>
    ${p('如果是非常具体的技术对象，再补一句：注意避免重名项目，查询里带 owner/repo、官方域名、包名或关键 benchmark 数字。')}

    ${h2('五、这次留下的边界')}
    <section style="${S.quote}">Brave 这次还不能进入最终排名，因为本机没有完整 API key，网页版又出现 429。DeepSeek Chat API 也不能替代搜索，它只能解释已经找到的证据。</section>
    ${p('所以最终工作流不是“找一个最强工具”，而是把工具排成顺序：AnySearch 找出处，Tavily 交叉验证，模型解释和写作。')}
  </section>
</body>
</html>`;

const outPath = path.join(outDir, 'anysearch-comparison-wechat-single-column.html');
fs.writeFileSync(outPath, html, 'utf8');
console.log(JSON.stringify({ outPath, assets: assets.map(a => path.join(assetDir, a)) }, null, 2));
