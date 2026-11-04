// Responsive check for every page at common screen widths.
// Run from the repo root while `python3 -m http.server 8765` is serving it:
//   node checks/responsive.js
// Fails if any page scrolls sideways or any element sticks out past the screen edge.
const { chromium } = require('playwright');
const pages = ['/', '/services/', '/services/pattern-audit/', '/services/growth-strategy/',
  '/services/scale-strategy/', '/services/communication-strategy/', '/about/', '/book/', '/thanks/', '/404.html'];
const widths = [320, 360, 390, 430, 768, 1024, 1280, 1440, 1920];
(async () => {
  const browser = await chromium.launch();
  let problems = 0;
  for (const w of widths) {
    const page = await browser.newPage({ viewport: { width: w, height: 900 } });
    for (const path of pages) {
      await page.goto('http://localhost:8765' + path, { waitUntil: 'load' });
      const r = await page.evaluate(() => {
        const vw = document.documentElement.clientWidth, out = [];
        document.querySelectorAll('body *').forEach(el => {
          const b = el.getBoundingClientRect(), cs = getComputedStyle(el);
          if (!b.width || cs.position === 'fixed' || el.closest('.marquee, .skip, [aria-hidden="true"], #cal-inline')) return;
          if (b.right > vw + 1 || b.left < -1) out.push(el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ')[0] : ''));
        });
        return { sw: document.documentElement.scrollWidth, vw, out: [...new Set(out)].slice(0, 5) };
      });
      if (r.sw > r.vw || r.out.length) { problems++; console.log(`FAIL ${w}px ${path} scrollWidth=${r.sw} overflow: ${r.out.join(', ')}`); }
    }
    await page.close();
  }
  await browser.close();
  console.log(problems ? `${problems} problem(s)` : `All ${pages.length} pages pass at ${widths.join(', ')}px`);
  process.exit(problems ? 1 : 0);
})();
