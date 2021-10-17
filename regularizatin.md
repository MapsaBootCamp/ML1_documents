<html  dir="rtl" lang="fa-IR"> </html>

# <p style="color:cyan" dir="ltr"> **Types of Regularization in Machine Learning** </p>

در این مقاله ما قصد داریم در مورد regularization و اینکه چرا به آن احتیاج داریم و انواع متفاوت در machine learning صحبت کنیم.

# <p style="color:cyan" dir="ltr"> **Why Regularization?** </p>

regularization اغلب به عنوان راه حلی برای رفع مشکل overfitting در یادگیری ماشین استفاده می شود.

overfitting به دلایل زیر اتفاق می‌افتد:

* هنگامی که مدل به اندازه کافی پیچیده است که در این مدل حتی noise ها هم مدنظر قرار گرفته‌اند.

* هنگامی که تعداد داده‌های trian کافی نیست و نشان دهت=نده ناکافی توزیع اصلی است که ازآن نمونه‌گیری  شده است. به عبارتی دیگر مدل نتوانسته مدلی با قابلیت تعیمم پذیری باشد و این را بیاموزد.

![Overfitting in Machine Learning ](https://miro.medium.com/max/2000/1*vCGSqy05QbiYhvdH4DXxBw.png)


**<p style="color:green"> Regularization به ما کمک می‌کند تا مسئله و مشکل overfitting را حل کنیم. </p>**

# <p style="color:cyan" dir="ltr"> **What is Regularization?** </p>
 
Regularization شامل تکنیک‌ها و روش‌های متفاوتی است که برای رفع و حل مشکل overfitting با کاهش generalization error بدون تاثیر زیاد بر خطای trian 
استفاده می‌شود.

انتخاب یک مدل بیش از حد پیچیده و دقیق برای داده‌های trian اغلب منجر به overfitting می‌شود. از سوی دیگر انتخاب یک مدل ساده و یا به عبارت دیگر نا‌دقیق  باعث بروز مشکل underfitting می‌شود.

**<p style="color:green"> بنابراین انتخاب میزان مناسب پیچیدگی و دقت در مدل برای دیتاهای trian بسیار مهم است.</p>**

از انجا که  پیچیدگی مدل را نمی‌توان مستقیم از داده های آموزش استنباط کرد، غالبا نمی‌توان پیچبدگی مناسب را برای داده های train استفاده کرد.
اینجاست که Regularization به میان می‌آید و پیچیدگی مستعد و درست را برای داده‌های train پیدا می‌کند.

# <p style="color:cyan" dir="ltr"> **Types of Regularization** </p>

بر اساس رویکردی که برای غلبه بر overfitting استفاده می‌شود،  می‌توانیم تکنیک های Regularization را بر اساس میزان موثر بودن در پرداختن به مسئله overfitting به دسته های زیر تقسیم کنیم:

* Strong (قوی)
* medium (متوسط)
* week (ضعیف)

___

## <p style="color:cyan" dir="ltr"> **1. Modify loss function:** </p>

در این روش regularization، تایع ضرر که تحت آن مدل بهینه شده است اصلاح می‌شود تا مستقیما توزیع خروجی را در نظر بگیرد. 

ما تکنیک‌های regularization مبتنی بر تابع  هزینه را داریم:

#### <p style="color:yellow" dir="ltr"> **a. L2 Regularization (strong):** </p>

مسئله linear regression را با mean squared loss در نظر بگیرید.


![regression with mean squared](https://miro.medium.com/max/875/1*lI-jrI2hMQiuRcDSokE5mw.png)

در regularization از نوع L2، ما تابع  هزینه را تغییر می‌دهیم تا شامل اصل و معیار L2 وزنی وزن‌های بهینه شده شود.

این امر از بزرگ شدن بیش از حد وزن ‌ها جلوگیری می‌کند و در نتیجه از  overfitting جلوگیری می کند.

![regression with mean squared](https://miro.medium.com/max/875/1*zFuomRDJFeqtMy1sbekywQ.png)

ثابت و شرط  لامبدا در فرمول بالا برای کنترل تناسب بین overfitting و underfitting استفاده می‌شود.


![regression with mean squared](https://miro.medium.com/max/875/1*lFmQebk5GoibKN2ZQYzYpw.png)

#### <p style="color:yellow" dir="ltr"> **b. L1 Regularization (strong):** </p>

به جای استفاده از قاعده L2  در  lost function در L1 Regularization  ما از قاعده ( قدر مطلق خطا) برای وزن ها استفاده می‌شود.

![regression with mean squared](https://miro.medium.com/max/875/1*P3bTxrYuLGhF5-m0WEgomQ.png)


#### <p style="color:yellow" dir="ltr"> **c. Entropy Regularization (strong):** </p>

آنتروپی توزیع احتمال را از نظر عدم قطعیت در آنها کمی می کند. هرچه عدم قطعیت در توزیع بیشتر باشد ، آنتروپی بیشتر است. توزیع یکنواخت احتمال وقوع همه رویدادهای آن برابر است ، به این معنی که میزان عدم قطعیت حداکثر و در نتیجه حداکثر آنتروپی است. از سوی دیگر ، توزیع ظاهری به این معنی است که اگر از چنین توزیعی از یک رویداد تصادفی نمونه برداری شود ، می دانیم که همیشه یک رویداد مشابه خواهد بود. بنابراین چنین توزیع تکانشی دارای حداقل آنتروپی است.

Entropy Regularization زمانی استفاده می‌شود که خروجی مدل یک توزیع احتمال باشد. برای مثال مسائل classification و غیره...

به جای استفاده مستقیم از قاعده وزن ها در تابع هزینه ما از Entropy regularizer که آنتروپی تابع خروجی را شامل می شود استفاده می کنیم.

![regression with mean squared](https://miro.medium.com/max/875/1*aMfwFD1vtCXIVuCfPpPxYA.png)

![regression with mean squared](https://miro.medium.com/max/875/1*e22QgKGc8ia9LwOmuBl0OQ.png)
___

## <p style="color:cyan" dir="ltr"> **2. Modify sampling method** </p>

از این روش‌ها برای غلبه بر Overfitting که به دلیل اندازه‌ی محدود داده موجود است، مفید است. در این روش Regularization تلاش می‌شود ورودی های موجود را دستکاری کرده و نمایشی عادلانه از توزیع ورودی واقعی ایجاد کرد.

در زیر دو روش Regularization که در این دسته قرار دارند آورده شده است.

#### <p style="color:yellow" dir="ltr"> **a. Data Augmentation (weak):** </p>

Data augmentation شامل افزایش حجم داده های موجود، با افزایش ورودی بیشتر به صورت مصنوعی است. ایده این است که به طور مشنوعی داده های بیشتری اسجاد شود به این امید که مجموعه داده‌های تقویت شده بازنمایی بهتری از توزیع پنهان اصلی باشد.

از آنجا که ما فقط با مجموعه داده های موجود محدود می‌شویم، این روش به طور کلی خوب عمل نمی کند.

![regression with mean squared](https://miro.medium.com/max/875/0*xfCOt_Wo0Pa9fodp.png)


#### <p style="color:yellow" dir="ltr"> **b. K-fold Cross-Validation (medium):** </p>

از این روش برای ایجاد چندین train dataset استفاده می‌شود و سپس شبکه ای را انتخاب می‌کند که کمترین خطای تعمیم را داشته باشد.

در اعتبار سنجی متقابل k-fold، مجموعه  داده‌های train به k زیرمجموعه تقسیم می‌شود و k مدل train می‌شوند.

برای هر مدل، یکی از زیر مجموعه ها برای تایید اعتبار استفاده می شوند در حالی مه بقیه زیر مجموعه‌های (k-1) برای آموزش استفاده می‌شوند.

هنگامی که همه مدل ها  train شدند , عملکرد همه ثبت شد مدل با بهترین معیار عمبکرد به عنوان مدل نهایی انتخاب می‌شود.

![regression with mean squared](https://miro.medium.com/max/875/1*ETZwPbOvu7AQF8ZVUcErzQ.png)

___

## <p style="color:cyan" dir="ltr"> **3. Modify training algorithm** </p>

Regularization می‌تاوند با اصلاح الگوریتم train به روش های مختلف پیدا سازی شود.
دو روش پرکاربرد را در زیر معرفی می‌کنیم.

#### <p style="color:yellow" dir="ltr"> **a. Dropout (strong)** </p>

Dropout زمانی استفاده می شود که مدل آموزشی یک شبکه عصبی باشد. یک شبکه عصبی از چندین لایه مخفی تشکیل شده است ، جایی که خروجی یک لایه به عنوان ورودی لایه بعدی استفاده می شود. لایه بعدی ورودی را از طریق پارامترهای قابل یادگیری تغییر می دهد (معمولاً با ضرب آن در ماتریس و اضافه کردن یک سوگیری به دنبال یک تابع فعال سازی). 

ورودی از لایه های شبکه عصبی عبور می کند تا به لایه خروجی نهایی برسد ، که برای پیش بینی استفاده می شود.
هر لایه در شبکه عصبی از گره های مختلفی تشکیل شده است. گره های لایه قبلی به گره های لایه بعدی متصل می شوند. در روش Dropout، اتصالات بین گره های لایه های متوالی به طور تصادفی بر اساس نسبت رها شده (درصد کل اتصال قطع شده) قطع می شود و شبکه باقیمانده در تکرار فعلی آموزش داده می شود. در تکرار بعدی ، مجموعه دیگری از اتصالات تصادفی حذف می شوند.

![regression with mean squared](https://miro.medium.com/max/875/1*WCP9F1g9PG4nlO-S4jMw9A.png)

#### <p style="color:yellow" dir="ltr"> **b. Injecting noise (weak)** </p>

مشابه روش Dropout ، این روش معمولاً زمانی استفاده می شود که مدل یاد گرفته شده یک شبکه عصبی باشد. در این روش ، ما وزنهایی را که از طریق انتشار مجدد یاد گرفته می شود ، دستکاری می کنیم تا بتوانیم آن را در برابر تغییرات کوچک قوی تر یا حساس تر کنیم. در طول آموزش ، مقدار کمی نویز تصادفی به وزنه های به روز شده اضافه می شود که به مدل کمک می کند مجموعه قوی تری از ویژگی ها را بیاموزد. مجموعه ای قوی از ویژگی ها اطمینان می دهد که مدل از داده های آموزشی overfit نیست. با این حال ، این روش چندان خوب عمل نمی کند.