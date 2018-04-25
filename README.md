# Webpage Title Checker

## Requirements
* Python
* BeautifulSoup4
  - `pip install beautifulsoup4`
* LXML
  - `pip install lxml`
  
## Usage
Add a CSV titled "urls.csv" into the same location of the script. The "urls.csv" file should have all the URLs you would like to check. This script grabs all `<title>` elements and will print "%s has too many title tags" if there are more than 1, or "%s has potentially no title tags" If there are 0.

To run, run `python url-check.py` from a terminal where the script is stored.
