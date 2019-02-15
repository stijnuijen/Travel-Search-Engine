# TravelSearch
## Information Retrieval project: travel search

Project for the University of Amsterdam course Information Retrieval 2018/2019. Implements a simple search engine for travel information.

Crawling is implemented with scrapy, which follows the following file structure. All spiders, which are responsible for crawling a particular website, reside in the folder project/spiders/.
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