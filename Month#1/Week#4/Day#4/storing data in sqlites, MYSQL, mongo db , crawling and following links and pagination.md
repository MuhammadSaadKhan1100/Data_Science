# Storing data in sqlites:
![image](https://user-images.githubusercontent.com/112848881/191803053-bf35a6f6-9f9a-4c07-b0f1-2d048c8de03f.png)

# Pipelines.py:
```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3
class QuotetPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn = sqlite3.connect("my_quotes.db")
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                            title text,
                            author text,
                            tag text
                            )""")

    def process_item(self, item, spider):
        print("Pipelines: "+ item['title'][0])
        return item

    def store_db(self,item):
        self.curr.execute("""insert into quotes_tb values (?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
```
# Data storage in MYSQL  🟦🟨:
```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector


class QuotetPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1helloworld',
            database='myquotes'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                            title text,
                            author text,
                            tag text
                            )""")

    def process_item(self, item, spider):
        print("Pipelines: " + item['title'][0])
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into table quotes_tb """, (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()

```
# Crawling and Following links  🦀👶:
# Code:
```python
import scrapy
from ..items import QuotetItem


class Quotes_to_scrape(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response):
            items = QuotetItem()
            all_div_quotes = response.css('div.quote')
            for quotes in all_div_quotes:
                title = quotes.css('span.text::text').extract()
                author = quotes.css('.author::text').extract()
                tag = quotes.css(".tag::text").extract()

                items['title'] = title
                items['author'] = author
                items['tag'] = tag

                yield items

            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse)
```
# Random Output:
![image](https://user-images.githubusercontent.com/112848881/191797293-1c2eba8f-8f09-45ec-84ce-8820a69c912e.png)

# Pagination  📃📄📟:
* Pagination is the art of scraping next pages
* General syntax:
* ![image](https://user-images.githubusercontent.com/112848881/191802476-8aad16e7-fb49-458f-812c-602a24520dc2.png)
# Code 💻:
```python
import scrapy
from ..items import QuotetItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/page/1/"
    ]
    def parse(self, response):
            items = QuotetItem()
            all_div_quotes = response.css('div.quote')
            for quotes in all_div_quotes:
                title = quotes.css('span.text::text').extract()
                author = quotes.css('.author::text').extract()
                tag = quotes.css(".tag::text").extract()

                items['title'] = title
                items['author'] = author
                items['tag'] = tag

                yield items

            next_page = "https://quotes.toscrape.com/page/" + str(QuoteSpider.page_number) + '/'
            print(next_page)
            if QuoteSpider.page_number < 11:
                QuoteSpider.page_number += 1
                yield response.follow(next_page, callback = self.parse)
```
# Random selected output:
![image](https://user-images.githubusercontent.com/112848881/191802856-f0abcec9-6d61-4cc7-9a02-f082774548ca.png)
* 🔚


