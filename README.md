# Zebrafish oocyte analysis

The goal of this project is to analyze glycogen molecules in zebrafish oocytes.

## Getting started

### Installation

This project uses uv to manage Python versions and installations. 

1. Install uv
* **macOS / Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
* **Windows (PowerShell):** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

2. Clone (or download) the repository
```bash
git clone git@github.com:vaioic/burton-lab-zebrafish-oocyte-analysis.git
cd burton-lab-zebrafish-oocyte-analysis
```

3. Sync the environment (this will download the dependencies)
```bash
uv sync
```

3. Run the analysis
```
uv run analyze_images.py
```

## Issues

If you encounter any issues with running the code or have any questions, please create an [Issue](https://github.com/vaioic/burton-lab-zebrafish-oocyte-analysis/issues) or send an email to opticalimaging@vai.org. If you are reporting a bug, please include any error messages to aid with troubleshooting.