<div dir="rtl">
 
 # الگوریتم KMP
 
 <span style="color: blue"> hello </span>
 
الگوریتم تطبیق KMP از خاصیت تقسیم الگو (الگویی که دارای همان الگوی فرعی است که بیش از یک بار در الگو ظاهر می شود) و بهبود بدترین حالت برای O (n) استفاده میکند.

ایده اصلی در پشت الگوریتم KMP این است که: هر زمان که عدم تطابق را تشخیص دادیم (بعد از چند مورد منطبق)، با دانستن برخی از کاراکترهای متن که در پنجره بعدی وجود دارند با استفاده از این اطلاعات از انجام فرآیندی انطباق برای کارکتر هایی که از انطباق آن ها اطمینان داریم جلوگیری میکنیم.
## نحوه عمالکرد الگوریتم
- ابتدا برای بررسی گام زمانی برای پایش متن احتیاج به پیش پردازش الگو جستجو برای یافتن پیشوند ها و پسوند ها هستیم تا نحوه تکرار کارکتر ها در الگو را در یک لیست ذخیره کنیم.
- سپس با توجه به تکرار پیشوند ها در پسوند ها با توجه به تطابق متن با الگو و لیست پیش پردازش ساخته شده گام های جستجو تعیین می شود.
### عملیات پیش پردازش 
برای تعیین لیست پیشوند های مناسب که در پسوند ها  (LPS) تکرار شده اند ابتدا لازم است که در پیمایش در الگو انجام گیرد که بطور معمول درایه اول برای همه الگو ها برابر 0 می باشد. سپس با مقایسه هر کارکتر با ابتدای لیست در صورت تکرار پیشوند در پسوند مقدار 1 را به آن درایه از لیست تا جایی که تکرار الگوی پیشوندی ادامه دارد اضافه می کنیم و اگر کارکتر متفاوت ظاهر شد مقدار 1 را از آن کم می کنیم تا پیمایش الگو به انتها برسد. برای فهم بهتر شکل زیر را مشاهد کنید:
</div>

![LPS](https://miro.medium.com/max/700/1\*OIb4erqMedwaze8aTUi9gw.gif)


<div dir="rtl">
 
همچنین مثال زیر برای محاسبه پیش پردازش الگو نشان داده شده است:
 
</div>
  
  
```

pat[] = "**AAACAAAA**"

len = 0, i  = 0.

**lps[0] is always 0**, we move 

to i = 1

len = 0, i  = 1.

Since pat[len] and pat[i] match, do len++, 

store it in lps[i] and do i++.

len = 1, **lps[1] = 1**, i = 2

len = 1, i  = 2.

Since pat[len] and pat[i] match, do len++, 

store it in lps[i] and do i++.

len = 2, **lps[2] = 2**, i = 3

len = 2, i  = 3.

Since pat[len] and pat[i] do not match, and len > 0, 

set len = lps[len-1] = lps[1] = 1

len = 1, i  = 3.

Since pat[len] and pat[i] do not match and len > 0, 

len = lps[len-1] = lps[0] = 0

len = 0, i  = 3.

Since pat[len] and pat[i] do not match and len = 0, 

Set **lps[3] = 0** and i = 4.

We know that characters pat

len = 0, i  = 4.

Since pat[len] and pat[i] match, do len++, 

store it in lps[i] and do i++.

len = 1, **lps[4] = 1**, i = 5

len = 1, i  = 5.

Since pat[len] and pat[i] match, do len++, 

store it in lps[i] and do i++.

len = 2, **lps[5] = 2**, i = 6

len = 2, i  = 6.

Since pat[len] and pat[i] match, do len++, 

store it in lps[i] and do i++.

len = 3, **lps[6] = 3**, i = 7

len = 3, i  = 7.

Since pat[len] and pat[i] do not match and len > 0,

set len = lps[len-1] = lps[2] = 2

len = 2, i  = 7.

Since pat[len] and pat[i] match, do len++, 

store it in lps[i] and do i++.

len = 3, **lps[7] = 3**, i = 8

We stop here as we have constructed the whole lps[].

```

<div dir="rtl">
 
### عملیات جستجو
در این بخش مانند الگوریتم naive ابتدا تطابق الگو و متن را بررسی می کنیم و درصورتی که به عدم تطابق برسیم درایه کارکتری از الگو که به عدم تطابق رسیده است را مساوی با گام متناظر همان درایه-1 برابر گرفته و دوباره عملیات جستجو را از سر می گیریم تا نهایتا به انتهای متن برسیم. این کار باعث کاهش پیمایش در متن برای الگو هایی که پیشوند و پسوند های مشابه دارند می شود. شکل زیر نشان دهنده عملکرد این الگوریتم با استفاده از لیست LPS می باشد.

</div>
  
![kmp](https://miro.medium.com/max/700/1\*hGaxEHtNvfYJDxHeFV171g.png)

![kmp](https://miro.medium.com/max/700/1\*kPepYjAnJqlP495bjI0p8w.png)

<div dir="rtl">
 
در مثال زیر نیز نحوه عملکرد این الگوریتم نشان داده شده است:

</div>

```

txt[] = "**AAAA**ABAAABA" 

pat[] = "**AAAA**"

lps[] = {0, 1, 2, 3} 

i = 0, j = 0

txt[] = "**AAAA**ABAAABA" 

pat[] = "**AAAA**"

txt[i] and pat[j] match, do i++, j++

i = 1, j = 1

txt[] = "**AAAA**ABAAABA" 

pat[] = "**AAAA**"

txt[i] and pat[j] match, do i++, j++

i = 2, j = 2

txt[] = "**AAAA**ABAAABA" 

pat[] = "**AAAA**"

pat[i] and pat[j] match, do i++, j++

i = 3, j = 3

txt[] = "**AAAA**ABAAABA" 

pat[] = "**AAAA**"

txt[i] and pat[j] match, do i++, j++

i = 4, j = 4

Since j == M, print **pattern found** and reset j,

j = lps[j-1] = lps[3] = 3

Here unlike Naive algorithm, we do not match first three 

characters of this window. Value of lps[j-1] (in above 

step) gave us index of next character to match.

i = 4, j = 3

txt[] = "A**AAAA**BAAABA" 

pat[] =  "**AAAA**"

txt[i] and pat[j] match, do i++, j++

i = 5, j = 4

Since j == M, print **pattern found** and reset j,

j = lps[j-1] = lps[3] = 3

Again unlike Naive algorithm, we do not match first three 

characters of this window. Value of lps[j-1] (in above 

step) gave us index of next character to match.

i = 5, j = 3

txt[] = "AA**AAAB**AAABA" 

pat[] =   "**AAAA**"

txt[i] and pat[j] do NOT match and j > 0, change only j

j = lps[j-1] = lps[2] = 2

i = 5, j = 2

txt[] = "AAA**AABA**AABA" 

pat[] =    "**AAAA**"

txt[i] and pat[j] do NOT match and j > 0, change only j

j = lps[j-1] = lps[1] = 1 

i = 5, j = 1

txt[] = "AAAA**ABAA**ABA" 

pat[] =     "**AAAA**"

txt[i] and pat[j] do NOT match and j > 0, change only j

j = lps[j-1] = lps[0] = 0

i = 5, j = 0

txt[] = "AAAAA**BAAA**BA" 

pat[] =      "**AAAA**"

txt[i] and pat[j] do NOT match and j is 0, we do i++.

i = 6, j = 0

txt[] = "AAAAAB**AAABA**" 

pat[] =       "**AAAA**"

txt[i] and pat[j] match, do i++ and j++

i = 7, j = 1

txt[] = "AAAAAB**AAAB**A" 

pat[] =       "**AAAA**"

txt[i] and pat[j] match, do i++ and j++

We continue this way...

```

<div dir="rtl">
 
## پیچیدگی محاسباتی
این الگوریتم پیچیدگی محاسباتی را برای بدترین حالت الگوریتم Naive را تا O(m+n) کاهش می دهد و باعث کاهش محاسبات و انجام محاسبات تکراری میشود.
### مزایا:
- بهبود استفاده از زمان پردازش و حافظه در الگو هایی که شامل کارکتر های تکراری می باشند.
## معایب:
- افزایش محاسبات بدلیل وجود پیش پردازش در الگو هایی که کارکتر های مشابه ندارند.

</div>
