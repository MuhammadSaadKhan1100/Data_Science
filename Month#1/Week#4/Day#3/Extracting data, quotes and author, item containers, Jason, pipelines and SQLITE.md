# Extracting data, quotes and author: 💱📅
![image](https://user-images.githubusercontent.com/112848881/191587190-3a80a781-874d-4999-bbf8-f3ff5b88f77e.png)

# Code: 💻
```python
import scrapy
class Quotes_to_scrape(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response):
            all_div_quotes = response.css('div.quote')
            for quota in all_div_quotes:
                title = quota.css('span.text::text').extract()
                author = quota.css('.author::text').extract()
                tag = quota.css(".tag::text").extract()

                yield {
                    'title' : title,
                    'author' : author,
                    'tag' : tag
                }
```
# Terminal_Output:
![image](https://user-images.githubusercontent.com/112848881/191527116-b8a332ca-4051-4621-a8e4-da7e4cfc9041.png)

# Item containers: 🍼
* Items are containers used to store data.
* We can put extracted data directly into our databases but there are some problems.
* These are temporary locations.
# quotes_spider.py:
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
```
# items.py:
```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()


```
# Terminal Output:
![image](https://user-images.githubusercontent.com/112848881/191536652-e3f244b1-3b45-4a58-af7f-5afed900571a.png)

# json file:
```python
[
{"title": ["\u201cThe world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.\u201d"], "author": ["Albert Einstein"], "tag": ["change", "deep-thoughts", "thinking", "world"]},
{"title": ["\u201cIt is our choices, Harry, that show what we truly are, far more than our abilities.\u201d"], "author": ["J.K. Rowling"], "tag": ["abilities", "choices"]},
{"title": ["\u201cThere are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.\u201d"], "author": ["Albert Einstein"], "tag": ["inspirational", "life", "live", "miracle", "miracles"]},
{"title": ["\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d"], "author": ["Jane Austen"], "tag": ["aliteracy", "books", "classic", "humor"]},
{"title": ["\u201cImperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.\u201d"], "author": ["Marilyn Monroe"], "tag": ["be-yourself", "inspirational"]},
{"title": ["\u201cTry not to become a man of success. Rather become a man of value.\u201d"], "author": ["Albert Einstein"], "tag": ["adulthood", "success", "value"]},
{"title": ["\u201cIt is better to be hated for what you are than to be loved for what you are not.\u201d"], "author": ["Andr\u00e9 Gide"], "tag": ["life", "love"]},
{"title": ["\u201cI have not failed. I've just found 10,000 ways that won't work.\u201d"], "author": ["Thomas A. Edison"], "tag": ["edison", "failure", "inspirational", "paraphrased"]},
{"title": ["\u201cA woman is like a tea bag; you never know how strong it is until it's in hot water.\u201d"], "author": ["Eleanor Roosevelt"], "tag": ["misattributed-eleanor-roosevelt"]},
{"title": ["\u201cA day without sunshine is like, you know, night.\u201d"], "author": ["Steve Martin"], "tag": ["humor", "obvious", "simile"]}
]
```
# csv file:
```python
author,tag,title
Albert Einstein,"change,deep-thoughts,thinking,world",“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
J.K. Rowling,"abilities,choices","“It is our choices, Harry, that show what we truly are, far more than our abilities.”"
Albert Einstein,"inspirational,life,live,miracle,miracles",“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
Jane Austen,"aliteracy,books,classic,humor","“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”"
Marilyn Monroe,"be-yourself,inspirational","“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”"
Albert Einstein,"adulthood,success,value",“Try not to become a man of success. Rather become a man of value.”
André Gide,"life,love",“It is better to be hated for what you are than to be loved for what you are not.”
Thomas A. Edison,"edison,failure,inspirational,paraphrased","“I have not failed. I've just found 10,000 ways that won't work.”"
Eleanor Roosevelt,misattributed-eleanor-roosevelt,“A woman is like a tea bag; you never know how strong it is until it's in hot water.”
Steve Martin,"humor,obvious,simile","“A day without sunshine is like, you know, night.”"

```
# xml file:
```python
<?xml version="1.0" encoding="utf-8"?>
<items>
<item><title><value>“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</value></title><author><value>Albert Einstein</value></author><tag><value>change</value><value>deep-thoughts</value><value>thinking</value><value>world</value></tag></item>
<item><title><value>“It is our choices, Harry, that show what we truly are, far more than our abilities.”</value></title><author><value>J.K. Rowling</value></author><tag><value>abilities</value><value>choices</value></tag></item>
<item><title><value>“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</value></title><author><value>Albert Einstein</value></author><tag><value>inspirational</value><value>life</value><value>live</value><value>miracle</value><value>miracles</value></tag></item>
<item><title><value>“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</value></title><author><value>Jane Austen</value></author><tag><value>aliteracy</value><value>books</value><value>classic</value><value>humor</value></tag></item>
<item><title><value>“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”</value></title><author><value>Marilyn Monroe</value></author><tag><value>be-yourself</value><value>inspirational</value></tag></item>
<item><title><value>“Try not to become a man of success. Rather become a man of value.”</value></title><author><value>Albert Einstein</value></author><tag><value>adulthood</value><value>success</value><value>value</value></tag></item>
<item><title><value>“It is better to be hated for what you are than to be loved for what you are not.”</value></title><author><value>André Gide</value></author><tag><value>life</value><value>love</value></tag></item>
<item><title><value>“I have not failed. I've just found 10,000 ways that won't work.”</value></title><author><value>Thomas A. Edison</value></author><tag><value>edison</value><value>failure</value><value>inspirational</value><value>paraphrased</value></tag></item>
<item><title><value>“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</value></title><author><value>Eleanor Roosevelt</value></author><tag><value>misattributed-eleanor-roosevelt</value></tag></item>
<item><title><value>“A day without sunshine is like, you know, night.”</value></title><author><value>Steve Martin</value></author><tag><value>humor</value><value>obvious</value><value>simile</value></tag></item>
</items>
```
# Using pipelines to store scrapped data:
* Main path will be
* scraped data -> Item containers -> pipelines -> SQL/Mongo databases
```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotetPipeline:
    def process_item(self, item, spider):
        print("Pipelines: "+ item['title'][0])
        return item

```
![image](https://user-images.githubusercontent.com/112848881/191552231-5e5692f4-f221-484c-b38b-7e00438a0885.png)

# Basics of SQLITE:
# CODE: 💻
```python
import sqlite3

conn = sqlite3.connect("myquotes.db")
curr = conn.cursor()
# curr.execute("""create table quotes_tb(
#             title text,
#             author text,
#             tag text
#             )""")

curr.execute("""insert into quotes_tb values('Python is awesome','buildwithpython','python')""")
conn.commit()
conn.close()
```
# sqlite table output:
![image](https://user-images.githubusercontent.com/112848881/191586419-dddb5640-5a73-4bf7-a1f9-b4f44ccf8cd5.png)

* 🔚
