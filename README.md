# TravelSearch
## Information Retrieval project: travel search
### Leon van Veldhuijzen (10817263), Stijn Uijen (10732969) & Jesse Haenen (10670742)

Project for the University of Amsterdam course Information Retrieval 2018/2019. Implements a simple search engine for travel information.

[Project demp](https://jessefh.github.io/travelsearch/)

Crawling is implemented with scrapy. The scrapy project follows the following file structure. All spiders, which are responsible for crawling a particular website, reside in the folder project/spiders/.

```
scrapy.cfg
project/
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        lonely_spider.py
        travelpoint_spider.py
        wiki_spider.py
```