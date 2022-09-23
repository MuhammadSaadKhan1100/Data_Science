# Login forms:
* We can also use python scraping inorder to login forms
* It can also be used to check out username and password
# Code:
```python
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]
    def parse(self, response):
        token = response.css('form input::attr(values)').extract()
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'fantasmaamante09@gmail.com',
            'password' : '1HelloWorld'
        }, callback = self.start_scraping)
    def start_scraping(self,response):
        open_in_browser(response)
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
# Inspecting login:
![image](https://user-images.githubusercontent.com/112848881/191961577-ac7c6dbd-db40-4c7e-b77a-bf90fd07e206.png)

# Website output:
![image](https://user-images.githubusercontent.com/112848881/191961885-d6ccfbf7-b4bd-4f69-b720-141465ef1152.png)

# Amazon Scraping:
