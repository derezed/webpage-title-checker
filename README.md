# Webpage Checker Tools

## url-check.py

### Requirements
* Python
* BeautifulSoup4
  - `pip install beautifulsoup4`
* LXML
  - `pip install lxml`
  
### Usage
Add a CSV titled "urls.csv" into the same location of the script. The "urls.csv" file should have all the URLs you would like to check. This script grabs all `<title>` elements and will print "%s has too many title tags" if there are more than 1, or "%s has potentially no title tags" If there are 0.

To run, run `python url-check.py` from a terminal where the script is stored.

## url-check-capital-letters.py

### Requirements
* Python
* BeautifulSoup4
  - `pip install beautifulsoup4`
* LXML
  - `pip install lxml`

### Usage
Add a CSV titled "capital-letters.csv" into the same location of the script. The CSV file should have all of the URLs you would like to check. This script iterates over each page in the spreadsheet and grabs all `<a>` tags on the page and checks their `href` attribute for any capital letters. Those links that contain capital letters are printed out for verfication that they should infact be capitalized.

To run, run `python url-check-capital-letters.py` from a terminal where the script is stored.
