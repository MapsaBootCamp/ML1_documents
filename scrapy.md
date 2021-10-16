# Scarpy

<p dir="rtl" align="right">

~~~text

اسکراپی یک چارچوب برنامه ای برای اسکرپ کردن وب سایت ها و استخراج داده های ساختار یافته است که می تواند برای طیف وسیعی از برنامه های مفید مانند داده کاوی ، پردازش اطلاعات یا بایگانی تاریخی استفاده شود.

~~~

اگرچه اسکراپی در ابتدا برای اسکرپ وب طراحی شده بود ، اما می توان از آن برای استخراج داده ها با استفاده از ای‌پی‌ای ها (مانند خدمات وب آمازون آمازون) یا به عنوان یک خزنده وب عمومی استفاده کرد.

___

## <p dir="rtl" lang="fa-IR"> <span style="color:Cyan"> **یک مثال برای اسپایدر** </span> </p>

<p dir="rtl" lang="fa-IR"> 
به منظور نشان دادن آنچه اسکراپی انجام می‌دهد و روی میز می‌آورد در باکس کد پایین نمونه و مثالی برای شما آورده ایم که با ساده‌ترین روش با استفاده از اسکراپی اسپایدر، اسپایدر به شما معرفی می‌شود.
</p>

<p dir="rtl" lang="fa-IR"> 
در باکس کد پایین اسپایدری وجود دارد که نقل قول های معروق سایت <p>http://quotes.toscrape.com</p> 

<p dir="rtl" lang="fa-IR"> 
را پس از صفحه بندی حذف می کند.
</p>


```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```
___ 

## <p dir="rtl" lang="fa-IR"><span style="color:Cyan">**اجرای برنامه**</span> </p>
<p dir="rtl" lang="fa-IR">
این را در یک فایل متنی قرار دهید ، نام آن را به عنوان quotes_spider.py بگذارید و عنکبوت را با استفاده از دستور runspider اجرا کنید: </p>

```text
scrapy runspider quotes_spider.py -o quotes.jl
```

<p dir="rtl" lang="fa-IR"> 
پس از اتمام این کار ، در فایل quotes.jl لیستی از نقل قول ها در قالب JSON Lines ، حاوی متن و نویسنده ، به این شکل را خواهید داشت:
<p>

```text
{"author": "Jane Austen", "text": "\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d"}
{"author": "Steve Martin", "text": "\u201cA day without sunshine is like, you know, night.\u201d"}
{"author": "Garrison Keillor", "text": "\u201cAnyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.\u201d"}
...
```
___


