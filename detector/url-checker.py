#!/usr/bin/env python3
"""url-checker.py - flag lookalike domains and scam URL patterns.

Educational tool by Srey Leak (sreyleak-security). MIT License.
No network calls: pure string heuristics. Review before trading, always.
"""
import re
import sys
from urllib.parse import urlparse

OFFICIAL_DOMAINS = {
      "polymarket.com",
}

# Common lookalike substitutions seen in workshop reports
LOOKALIKE_PAIRS = [
      ("rn", "m"), ("vv", "w"), ("0", "o"), ("1", "l"), ("5", "s"),
]

SCAM_KEYWORDS = [
      "recover", "refund-claim", "seed-verify", "airdrop-claim",
      "support-connect", "wallet-restore", "claim-reward",
]

def _swap_contains(host: str, a: str, b: str) -> bool:
      return a in host and host.replace(a, b) != host

def check(url: str) -> dict:
      host = urlparse(url if "://" in url else "https://" + url).hostname or ""
      host = host.lower().strip(".")
      issues = []

    # 1. Not an official domain at all
      official = any(host == d or host.endswith("." + d) for d in OFFICIAL_DOMAINS)
      if not official:
                issues.append(f"not-an-official-domain: {host}")

      # 2. Lookalike tricks even inside subdomains of officials
      for a, b in LOOKALIKE_PAIRS:
                if _swap_contains(host, a, b):
                              issues.append(f"lookalike-pair {a}->{b} in host: {host}")

            # 3. Scam keywords in path
            path = urlparse(url if "://" in url else "https://" + url).path.lower()
    for kw in SCAM_KEYWORDS:
              if kw in path:
                            issues.append(f"scam-keyword in path: {kw}")

          # 4. Homoglyph cyrillic 'а','е','о','р','с' in latin-looking host
          if re.search(r"[аеорсхѕіа\u0400-\u04FF]", host):
                    issues.append("possible-homoglyph-host")

    return {
              "url": url,
              "host": host,
              "verdict": "SUSPECT" if issues else "ok",
              "issues": issues,
    }

if __name__ == "__main__":
      if len(sys.argv) < 2:
                print("usage: url-checker.py <url> [<url>...]")
                sys.exit(1)
            for u in sys.argv[1:]:
                      r = check(u)
                      mark = "!!" if r["verdict"] == "SUSPECT" else "  "
                      print(f"{mark} {r['verdict']:8} {r['url']}")
                      for i in r["issues"]:
                                    print(f"      - {i}")
                        
