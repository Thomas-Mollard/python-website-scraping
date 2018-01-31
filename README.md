# python-website-scraping
Companion repository of the article ["How to scrape websites in 5 minutes ?"](http://blog.theodo.fr/2018/02/scrape-websites-5-minutes-scrapy/) in Theodo's blog

## Setup

- If you don't have `virtualenv` installed on your computer, install it using the [official documentation](https://virtualenv.pypa.io/en/stable/installation/)
- Setup a virtualenv with `virtualenv venv`
- Activate your virtualenv with `source venv/bin/activate`
- Install the required libraries with `pip install -r requirements.txt`

## Launch the crawlers

Within your virtual environment with Scrapy installed, you can run each Spider with `scrapy runspider selected_spider.py --output output_file.json`
