<div dir="rtl">
 
  **الگوریتم های هندسی**

این الگوریتم ها برای حل مسائل هندسی طراحی شده اند. برای حل آن ها نیاز به دانش عمیق در مورد موضوعات مختلق ریاضی مانند combinatorics، توپولوژی جبر، هندسی دیفرانسیلی و غیره می باشد.

**مثال1:**

**مختصات دو نقطه داده شده است. پیدا کردن شیب خط راست بین آن دو**
</div>

Input: 	     X1 = 4 ; y1 = 2

`     `X2 = 2 ; y2 = 5

Output:	     Slope is: -1.5 

<div dir="rtl">
برای محاسبه شیب یک خط تنها نیاز به داشتن مختصات دو نقطه از آن خط می باشد (x1, y1) و (x2, y2). 

فرمول مورد استفاده برای محاسبه شیب یک خط با استفاده از دو نقطه آن برابر است با:
</div>
Slope=m=y2-y1x2-x1

![Lightbox](Aspose.Words.fc03b999-63fc-4d1a-8e2c-9c0dc5a7988d.001.jpeg)

کد پایتون برای محاسبه شیب خط:
</div>
def slope(x1, y1, x2, y2):

`	`return float((y2-y1)/(x2-x1)




<div dir="rtl">

**مثال 2:**

**موقعیت مکانی بهینه یک نقطه برای به حداقل رساندن فاصله کلی**

یک مجموعه از نقاط و یک خط با فرمول ax+by+c=0 داده شده است. می خواهیم یک نقطه بر روی خط داده شده پیدا کنیم به طوریکه مجموع فاصله ها از مجموعه نقاط داده شده کمترین مقدار باشد. 
</div>

![Lightbox](Aspose.Words.fc03b999-63fc-4d1a-8e2c-9c0dc5a7988d.002.jpeg)

اگر ما یک نقطه در فاصله بینهایت بر روی خط داده شده انتخاب کنیم، پس فاصله کلی بینهایت خواهد شد. حالا اگر ما این نقطه را به سمت نقاط داده شده حرکت دهیم، فاصله کلی شروع به کاهش خواهد کرد. پس از آن با حرکت به سمت دیگر خط که آن نیز به سمت بینهایت می رود، مجموع فاصله کلی نیز دوباره شروع به افزایش می کند. بنابراین منحنی مجموع فاصله کلی همانند یک منحنی U شکل خواهد بود که ما می خواهیم نقطه پایین این منحنی را پیدا کنیم. 

به دلیل آنکه منحنی U شکل به صورت یکنواخت افزایش یا کاهش نمی یابد، ما نمیتوانیم از جستجوی باینری برای پیدا کردن نقطه مینیمم آن استفاده کنیم. در اینجا ما از جستجوی ternary (سه بعدی) برای پیدا کردن مینیمم فاصله از اکثر خط ها استفاده می کنیم. جستجوی سه بعدی در هر بار تکرار یک سوم فضای جستجو را کاهش می دهد. 

برای حل این مساله به شکل زیر عمل میکنیم. 

ما با مقادیر اولیه کم و زیاد به عنوان کوچکترین و بزرگترین مقادیر شروع می کنیم. سپس تکرار را شروع می کنیم. در هربار تکرار دو مقدار میانه (mid) را محاسبه می کنیم. Mid1 و mid2 که بیانگر موقعیت یک سوم و دو سوم در فضای جستجو هستند. سپس ما فاصله کلی تمامی نقاط را با استفاده از mid1 و mid2 محاسبه کرده و با مقایسه فاصله از این نقاط، مقادیر اولیه کم یا زیاد را به روزرسانی می کنیم. این تکرار تا زمانی که مقدار اولیه کم و زیاد تقریبا برابر شوند ادامه می یابد. 
  
</div>

\# A Python3 program to find optimum location

\# and total cost

import math

class Optimum\_distance:

`	`# Class defining a point

`	`class Point:

`		`def \_\_init\_\_(self, x, y):



`			`self.x = x

`			`self.y = y



`	`# Class defining a line of ax + by + c = 0 form

`	`class Line:



`		`def \_\_init\_\_(self, a, b, c):



`			`self.a = a

`			`self.b = b

`			`self.c = c



`	`# Method to get distance of point

`	`# (x, y) from point p

`	`def dist(self, x, y, p):



`		`return math.sqrt((x - p.x) \*\* 2 + (y - p.y) \*\* 2)



`	`# Utility method to compute total distance

`	`# all points when choose point on given

`	`# line has x-coordinate value as X

`	`def compute(self, p, n, l, x):



`		`res = 0



`		`y = -1 \* (l.a\*x + l.c) / l.b



`		`# Calculating Y of choosen point

`		`# by line equation

`		`for i in range(n):

`			`res += self.dist(x, y, p[i])



`		`return res



`	`# Utility method to find minimum total distance

`	`def find\_Optimum\_cost\_untill(self, p, n, l):



`		`low = -1e6

`		`high = 1e6



`		`eps = 1e-6 + 1





`		`# Loop untill difference between low

`		`# and high become less than EPS

`		`while((high - low) > eps):



`			`# mid1 and mid2 are representative x

`			`# co-ordiantes of search space

`			`mid1 = low + (high - low) / 3

`			`mid2 = high - (high - low) / 3



`			`dist1 = self.compute(p, n, l, mid1)

`			`dist2 = self.compute(p, n, l, mid2)



`			`# If mid2 point gives more total

`			`# distance, skip third part

`			`if (dist1 < dist2):

`				`high = mid2



`			`# If mid1 point gives more total

`			`# distance, skip first part

`			`else:

`				`low = mid1



`		`# Compute optimum distance cost by

`		`# sending average of low and high as X

`		`return self.compute(p, n, l, (low + high) / 2)



`	`# Method to find optimum cost

`	`def find\_Optimum\_cost(self, p, l):



`		`n = len(p)

`		`p\_arr = [None] \* n



`		`# Converting 2D array input to point array

`		`for i in range(n):

`			`p\_obj = self.Point(p[i][0], p[i][1])

`			`p\_arr[i] = p\_obj



`		`return self.find\_Optimum\_cost\_untill(p\_arr, n, l)



\# Driver Code

if \_\_name\_\_ == "\_\_main\_\_":



`	`obj = Optimum\_distance()

`	`l = obj.Line(1, -1, -3)



`	`p = [ [ -3, -2 ], [ -1, 0 ],

`		`[ -1, 2 ], [ 1, 2 ],

`		`[ 3, 4 ] ]



`	`print(obj.find\_Optimum\_cost(p, l))



\# This code is contributed by Sulu\_mufi

Output:

20.7652
