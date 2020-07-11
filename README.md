# getpaper [![Python](https://img.shields.io/badge/Python-3%2B-blue.svg)](https://www.python.org)

## Description 

`getpaper` is a package based on SciHub and Google Scholar that can download papers based on DOI or website address. It can also download related papers given keywords. 

## Setup

```python3
pip install -r requirements.txt
```

## Features & Usage

0. Initialization

```python3
from getpaper import GetPaper

gp = GetPaper()
```

1. Download single paper given DOI or website address. 

```python3
# set single paper with doi or address
gp.paper("10.1126/science.abc7424")
gp.paper("https://science.sciencemag.org/content/early/2020/06/15/science.abc7424.abstract")
gp.download()
```

Notes: 
- `getpaper` will not download duplicate articles;
- Once downloaded, all stored DOI will be cleared;
- For `download` function, `direction` argument is the current location by default;
- Downloaded article is named as "year-month-day-hour-minute-second.pdf".

2. Download related papers given keywords. Keywords can be article names, research fields or author names. 

```python3
gp.search("Deep Dive into Machine Learning Models for Protein Engineering")
gp.search("SARS, Computation", num_of_page=2)
gp.search("Roberta Croce")
gp.download()
```

Notes: 
- `num_of_page` is the corresponding number of page in Google Scholar. 
- `num_of_page`is 1 by default. 

## License

MIT
