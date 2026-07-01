# Zebrafish oocyte analysis

The goal of this project is to analyze glycogen molecules in zebrafish oocytes.

## Getting started

### Installation

#### Using uv (Recommended)

This project uses [uv](https://docs.astral.sh/uv/) to manage virtual environments and dependencies.

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
    uv run .\analysis\analyze_images.py
    ```

#### Using venv and pip

1. Clone (or download) the repository
    ```bash
    git clone git@github.com:vaioic/burton-lab-zebrafish-oocyte-analysis.git
    cd burton-lab-zebrafish-oocyte-analysis
    ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   ```

3. Activate the environment
   ```bash
   # macOS/Linux
   source ./venv/bin/activate

   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```

4. Install the repository as an editable module
   ```bash
   python -m pip install -e .
   ```

5. Run the analysis script
   ```bash
   python -m analysis.analysis_script

   # or
   python analysis/analysis_script.py
   ```


## Issues

If you encounter any issues with running the code or have any questions, please create an [Issue](https://github.com/vaioic/burton-lab-zebrafish-oocyte-analysis/issues) or send an email to opticalimaging@vai.org. If you are reporting a bug, please include any error messages to aid with troubleshooting.

## License

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.

## Citing & Acknowledgements

This repository is publicly available for open-source use, but it is developed and maintained by the Optical Imaging Core at the Van Andel Institute. If code from this repository contributed to data used in a publication, abstract, or presentation, please cite and acknowledge our work based on your affiliation:

### For External Users
Please cite this repository and acknowledge the author(s) in your publication's materials, methods, or acknowledgements section:
> "Image analysis pipelines were adapted from open-source tools developed by the Optical Imaging Core at the Van Andel Institute (GitHub:[burton-lab-zebrafish-oocyte-analysis](https://github.com/vaioic/burton-lab-zebrafish-oocyte-analysis))."

If you require custom adjustments or advanced analysis support, please contact us at opticalimaging@vai.org.

### For Internal Users & Close Collaborators
If you are an internal researcher or an external collaborator working directly with our staff, please include our Research Resource Identifier (RRID) in your materials and methods section:
> "Image analysis and data processing were performed in collaboration with the Optical Imaging Core at the Van Andel Institute (RRID:SCR_021968)."

Please review the Acknowledgement and Authorship Guidelines on [VAI's Core Technology and Services website](https://vanandelinstitute.sharepoint.com/sites/Cores/SitePages/Acknowledgements-and-Authorship.aspx)

### Contributors
<a href="https://github.com/vaioic/burton-lab-zebrafish-oocyte-analysis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vaioic/burton-lab-zebrafish-oocyte-analysis" />
</a>

## Changelog

### v0.2.0 (2026-07-01)
* Updated code to use ``uv``
* Added code to obtain preliminary data ([OIC-304](https://varioic.atlassian.net/browse/OIC-304))

### v0.1.0 (2026-06-24)
* Initial commit with preliminary code ([OIC-304](https://varioic.atlassian.net/browse/OIC-304))