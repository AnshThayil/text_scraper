# text_scraper

## Requirements Installation

- **Description**: To install the required packages, run the following command:
- **Usage**:
  ```bash
  pip install -r requirements.txt
  ```

  You must also install the following dependencies - 

  * [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
  * [GhostScript](https://ghostscript.com/releases/gsdnld.html)
  * [ImageMagick](https://imagemagick.org/script/download.php)

  After installing the libraries, add the `tesseract_path` variable to the `.env` file in the root directory which points to the `tesseract.exe` file on your system.


## Running the script
The script can be run in two modes
### 1. `--url` mode

- **Description**: This script extracts the text from a given URL.
- **Usage**: 
  ```bash
  python pdf_scraper.py --url <url>
  ```

### 2. `--txt` mode

- **Description**: This script extracts the text from a list of URLs in a given text file.
- **Usage**: 
  ```bash
  python pdf_scraper.py --txt <text file>
  ```