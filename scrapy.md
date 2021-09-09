<div dir="rtl">

# scrapy
<p>
 وب اسکرپینگ (web scraping) یک روش موثر برای جمع آوری داده ها از صفحات وب است و به ابزاری موثر در علم داده تبدیل شده است. کتابخانه های مختلفی مانند beautifulsoup در پایتون برای وب اسکرپ وجود دارد که سبب بهبود عملکرد دانشمندان داده می شوند. Scrapy یک چارچوب وب قدرتمند است که برای استخراج، پردازش و ذخیره داده ها استفاده می شود.
</p>
<p align="center">
<img  src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/09/scrapy.png">
</p>
<font size=6 color='red'>
scrapy چیست؟
</font>
<p>
Scrapy یک چارچوب وب کراولینگ (web crawling) رایگان و منبع باز است که به زبان پایتون نوشته شده است. این چارچوب در ابتدا برای انجام وب اسکرپینگ طراحی شده بود، اما می تواند برای استخراج داده ها با استفاده از API ها نیز مورد استفاده قرار گیرد.
</p>
<p>
Scrapy یک پکیج کامل برای دانلود صفحات وب، پردازش و ذخیره داده ها در پایگاه داده است.
</p>
<p>
وقتی صحبت از اسکرپینگ وب با چندین روش اسکرپ کردن وب سایت می شود، Scrapy مانند یک نیروگاه قدرتمند است. Scrapy کارهای بزرگتری را با سهولت انجام می دهد و صفحات متعدد یا گروهی از آدرس های اینترنتی را در کمتر از یک دقیقه اسکرپ می کند.
</p>
<p>
Scrapy قرارداد spider را فراهم می کند که به ما امکان می دهد کراولرهای (crawlers) عمومی و همچنین عمیق ایجاد کنیم. Scrapy همچنین خطوط لوله ای (item pipelines) را برای ایجاد توابع در spider فراهم می کند که می تواند عملیات مختلفی مانند جایگزینی مقادیر داده ها و غیره را انجام دهد.
</p>
<p align="center">
<img  src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/09/2019-09-06-11_44_51-Window.png">
</p>
<p>
<font size=6 color='red'>
web crawler چیست؟
</font>
</p>
<p>
web crawler (کراولر یا خزنده وب) برنامه ای است که به طور خودکار اسناد را در وب جستجو می کند. آنها در درجه اول برای اقدامات تکراری برای مرور (browsing) خودکار برنامه ریزی شده اند.
</p>
<p>
<font size=5 color='green'>
web crawler چگونه کار می کند؟
</font>
</p>
<p>
web crawler کاملاً شبیه یک کتابدار است. به دنبال اطلاعات موجود در وب سایت است، اطلاعات را دسته بندی کرده و سپس اطلاعات مربوط به اطلاعات کراول شده (crawled) را ایندکس گذاری و فهرست بندی می کند تا بر این اساس بازیابی و ذخیره شوند.
</p>
<p>
عملیاتی که توسط کراولر انجام می شود از قبل ایجاد می شود ، سپس کراولر تمام آن عملیات را به صورت خودکار انجام می دهد که یک ایندکس ایجاد می کند. با استفاده از یک نرم افزار خروجی می توان به ایندکس ها دسترسی پیدا کرد.
</p>
<p>
<font size=6 color='red'>
چگونه می توان Scrapy را نصب کرد؟
</font>
</p>
<p>
در محیط conda از دستور زیر برای نصب scrapy استفاده می شود:

<div align="left">

```
conda install -c conda-forge scrapy
```
</div>

همچنین می توان از محیط pip برای نصب scrapy استفاده کرد:

<div align="left">

```
pip install scrapy
```
</div>
Scrapy با پایتون نوشته شده است و ممکن است به چند پکیج پایتون مانند موارد زیر وابستگی داشته باشد:

* lxml: این یک تجزیه کننده(parser) XML و HTML کارآمد است.
* parcel: یک کتابخانه استخراج HTML/XML که در بالا روی lxml نوشته شده است.
* W3lib: این یک راهنمای چند منظوره برای کار با URL ها و کدگذاری صفحات وب است.
* twisted: یک چارچوب شبکه ناهمگام
* cryptography: این به نیازهای امنیتی مختلف در سطح شبکه کمک می کند.
</p>

<p>
<font size=6 color='red'>
ساختن اولین پروژه Scrapy
</font>
</p>
<p>
برای شروع اولین پروژه scrapy، به دایرکتوری یا مکانی که می خواهید فایل های خود را در آن ذخیره کنید بروید و دستور زیر را اجرا کنید
<p>
<div align="left">

```
scrapy startproject projectname
```
</div>
<p>
پس از اجرای این دستور ، دایرکتوری های زیر ایجاد شده در آن مکان را دریافت خواهید کرد.
</p>
</div>

* projectname/
 * scrapy.cfg: it deploys configuration file
* projectname/
 * __ init __.py: projects’s python module
 * items.py: project items definition file
 * middlewares.py: project middlewares file
 * pipelines.py: project pipelines file
 * settings.py: project settings file
* spiders/
 * __ init __.py: a directory where later you will put your spiders

<div dir="rtl">
<font size=6 color='red'>
ساختن اولین Spider
</font>
</p>
<p>
spider ها کلاس هایی هستند که ما تعریف می کنیم و از آنها برای جمع آوری اطلاعات از وب استفاده می کنیم. می بایست زیر کلاس scrapy.Spider و درخواست های اولیه برای ایجاد را تعریف کنیم.

کد spider خود را در یک فایل پایتون جداگانه می نویسیم و آن را در دایرکتوری projectname/spiders در پروژه خود ذخیره می کنیم.
</p>
</div>
<div align="left">

quotes_spider.py
``` python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_request(self):
          urls = [ '<a href="http://quotes.toscrape.com/page/1/">http://quotes.toscrape.com/page/1/</a>',
                       http://quotes.toscrape.com/page/2/,
                     ]
          for url in urls:
              yield scrapy.Request(url=url , callback= self.parse)

def parse(self, response):
     page = response.url.split("/")[-2]
     filename = 'quotes-%s.html' % page
     with open(filename, 'wb') as f:
           f.write(response.body)
     self.log('saved file %s' % filename)
```
</div>
<div dir="rtl">
همانطور که می بینید، ما توابع مختلفی را در spider های خود تعریف کرده ایم،

* spider : name را شناسایی می کند، باید در طول پروژه منحصر به فرد باشد.
* () start_requests: باید درخواست (request) های تکرار شدنی (iterable) را برگرداند که spider شروع به کراول کردن با آنها می کند.
* () parse: این متدی است که برای رسیدگی به پاسخ (response) دانلود شده با هر درخواست، فراخوانی می شود.

<p>
<font size=6 color='red'>
استخراج داده ها
</font>
</p>
<p>
تا کنون spider هیچ داده ای را استخراج نمی کند، فقط کل فایل HTML را ذخیره کرده است. spider معمولاً بسیاری از دیکشنری ها را که حاوی داده های استخراج شده از صفحه وب است، تولید می کند. ما از کلمه کلیدی yield در python در فراخوانی برای استخراج داده ها استفاده می کنیم.
</p>
</div>

<div align="left">

``` python
import scrapy
class QuotesSpider(scrapy.Spider):

       name = "quotes"
       start_urls = [ http://quotes.toscrape.com/page/1/',
                             http://quotes.toscrape.com/page/2/,
                           ]

       def parse(self, response):
            for quote in response.css('div.quote'):
                  yield {
                              'text': quote.css(span.text::text').get(),
                              'author': quote.css(small.author::text')get(),
                              'tags': quote.css(div.tags a.tag::text').getall()
                             }
```
</div>
<div dir="rtl">

وقتی این spider را اجرا می کنید ، داده های استخراج شده را با log خروجی می دهد.

<p align="center">
<img  src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/09/2019-09-06-12_00_46-Window.png">
</p>
<p>
<font size=6 color='red'>
ذخیره داده ها
</font>
</p>
<p>
ساده ترین راه برای ذخیره داده های استخراج شده ، استفاده از خروجی فید (feed) است ، از دستور زیر برای ذخیره داده های خود استفاده کنید.
</p>
</div>


<div align="left">

```
scrapy crawl quotes -o quotes.json
```
</div>
<div dir="rtl">
<p>
این دستور یک فایل quotes.json شامل همه آیتم های اسکرپ شده ، سریال شده در JSON ایجاد می کند.
</p>
<p>
منبع: <a href="https://www.edureka.co/blog/scrapy-tutorial/">www.edureka.co</a>
</p>
</div>
