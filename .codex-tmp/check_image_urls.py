import concurrent.futures
import json
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
urls = [
    line.strip()
    for line in (ROOT / ".codex-tmp/new-supplier-image-urls.txt").read_text(
        encoding="utf-8"
    ).splitlines()
    if line.strip()
]


def check(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Range": "bytes=0-31",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return {
                "url": url,
                "ok": response.status in {200, 206},
                "status": response.status,
                "content_type": response.headers.get("Content-Type", ""),
                "final_url": response.geturl(),
            }
    except Exception as error:
        return {"url": url, "ok": False, "error": str(error)}


with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(check, urls))

summary = {
    "checked": len(results),
    "accessible": sum(result["ok"] for result in results),
    "failed": sum(not result["ok"] for result in results),
    "image_content_type": sum(
        result.get("content_type", "").startswith("image/") for result in results
    ),
    "final_http": sum(
        result.get("final_url", "").startswith("http://") for result in results
    ),
    "final_https": sum(
        result.get("final_url", "").startswith("https://") for result in results
    ),
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
failures = [result for result in results if not result["ok"]]
if failures:
    print(json.dumps(failures[:20], ensure_ascii=False, indent=2))
(ROOT / ".codex-tmp/image-check-results.json").write_text(
    json.dumps({"summary": summary, "results": results}, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
