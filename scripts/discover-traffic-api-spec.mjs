import { chromium } from "playwright";

const TARGET_URL =
  process.argv[2] ?? "https://developer.tomtom.com/traffic-api/api-explorer";

function looksLikeSpecUrl(url) {
  const u = url.toLowerCase();
  return (
    u.includes("openapi") ||
    u.includes("swagger") ||
    u.endsWith(".yaml") ||
    u.endsWith(".yml") ||
    u.endsWith(".json") ||
    u.includes("api-docs")
  );
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext();
const page = await context.newPage();

/** @type {Map<string, {status:number, contentType:string, size:number}>} */
const candidates = new Map();

page.on("response", async (resp) => {
  try {
    const url = resp.url();
    if (!looksLikeSpecUrl(url)) return;
    const status = resp.status();
    if (status < 200 || status >= 300) return;
    const headers = resp.headers();
    const contentType = headers["content-type"] ?? "";
    // Avoid grabbing large JS bundles; we only want data payloads.
    if (contentType.includes("javascript")) return;
    const buf = await resp.body();
    const size = buf?.byteLength ?? 0;
    // OpenAPI specs are typically at least a few KB.
    if (size < 1024) return;
    candidates.set(url, { status, contentType, size });
  } catch {
    // ignore
  }
});

await page.goto(TARGET_URL, { waitUntil: "domcontentloaded" });
// Let API Explorer bootstrap and fetch specs.
await page.waitForTimeout(10000);

// Try to provoke spec download by waiting for network idle.
await page.waitForLoadState("networkidle", { timeout: 30000 }).catch(() => {});

for (const [url, meta] of [...candidates.entries()].sort((a, b) => b[1].size - a[1].size)) {
  // Print as TSV for easy parsing.
  // url \t status \t contentType \t size
  process.stdout.write(`${url}\t${meta.status}\t${meta.contentType}\t${meta.size}\n`);
}

await browser.close();
