import json
from pathlib import Path


REPORT_DIR = Path(__file__).resolve().parents[1]
TRIVY_JSON = REPORT_DIR / "trivy.json"
REPORT_HTML = REPORT_DIR / "report.html"


def main():
    with TRIVY_JSON.open(encoding="utf-8") as report_file:
        data = json.load(report_file)

    count = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for result in data.get("Results", []):
        for vulnerability in result.get("Vulnerabilities") or []:
            severity = vulnerability.get("Severity", "UNKNOWN")
            if severity in count:
                count[severity] += 1

    html = f"""<h1>Docker CVE Report</h1>
<ul>
  <li>CRITICAL: {count['CRITICAL']}</li>
  <li>HIGH: {count['HIGH']}</li>
  <li>MEDIUM: {count['MEDIUM']}</li>
  <li>LOW: {count['LOW']}</li>
</ul>
"""
    REPORT_HTML.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
