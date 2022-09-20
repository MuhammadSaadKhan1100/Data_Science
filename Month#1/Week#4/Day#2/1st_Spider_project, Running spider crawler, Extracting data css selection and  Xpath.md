# 1st Spider project: 🕷🕸
* Website for scraping:
* ![image](https://user-images.githubusercontent.com/112848881/191349882-aa49d284-ec08-4284-897f-7bb589a99107.png)
# Code: 
```python
import scrapy
class Quote_spider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {"Titletext" : title }
```
# Terminal output:
![image](https://user-images.githubusercontent.com/112848881/191349436-18917209-2868-4023-be5f-683d039803e3.png)
# Extracting data using css selection:
![image](https://user-images.githubusercontent.com/112848881/191352201-5ad9eb89-606a-422b-934b-015ed6cf2073.png)
![image](https://user-images.githubusercontent.com/112848881/191354607-f9b595c6-e957-465f-8e26-0f2fae2a5a50.png)

# Extracting data using Xpath:
![image](https://user-images.githubusercontent.com/112848881/191359655-9a01267d-fcc8-4f46-8d9f-803f33f0e42b.png)
* 🔚
