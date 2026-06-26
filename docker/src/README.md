# Docker Security Scanner

A Python CLI tool that scans Docker images for vulnerabilities using Trivy and outputs a clean report of critical/high CVEs.

## ✨ Features
- Scans any Docker image via command line
- Parses Trivy JSON output for vulnerabilities 
- Filters to show only `CRITICAL` and `HIGH` severity issues
- Easy to use: no Docker knowledge needed to run the scanner

## 🛠️ Tech Stack
**Python, Trivy, Docker, JSON**

## 🚀 How to Run

1.  **Install dependencies**
    ```bash
    pip install -r requirements.txt