# getarticle [![Python](https://img.shields.io/badge/Python-3%2B-blue.svg)](https://www.python.org)

## Description 

`getarticle` is a package based on SciHub and Google Scholar that can download articles given DOI, website address or keywords.

## Install

1. PyPI

```
pip install getarticle
```

2. Git

```
git clone https://github.com/HTian1997/getarticle.git
```

## Setup

```python3
pip install -r requirements.txt
```

## Features & Usage

0. Initialization

```python3
from getarticle import GetArticle

ga = GetArticle()
```

1. Download a single article given DOI or website address. 

```python3
ga.article("10.1126/science.abc7424")
ga.download()
```

Notes: 
- Once downloaded, all stored articles will be cleared;
- For `download` function, `direction` argument is the current location by default;
- Downloaded article is named as "year-month-day-hour-minute-second.pdf".

2. Download multiple articles.

```python3
ga.article("https://www.nature.com/articles/s41594-020-0468-7#article-info")
ga.article("10.1038/s41893-020-0581-y")
ga.download()
```

Notes: 
- Repeatedly using `article` function can save multiple articles. 
- `getarticle` will not save & download duplicate articles;


3. Download related articles given keywords. Keywords can be article names, research fields or author names. 

```python3
ga.search("Deep Dive into Machine Learning Models for Protein Engineering")
ga.search("SARS, Computation", num_of_page=2)
ga.search("Roberta Croce")
ga.download()
```

Notes: 
- `num_of_page` is the corresponding number of page in Google Scholar. 
- `num_of_page` is 1 by default. 

## License

MIT
