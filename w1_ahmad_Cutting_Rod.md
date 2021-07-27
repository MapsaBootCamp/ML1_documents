# Cutting a Rod | DP-13
طول و آرایه از قیمت ها که شامل قیمت تمام قطعات در اندازه کوچکتر از n است .با برش میله و فروش قطعات حداکثر مقدار بدست آمده تعیین کنید. به عنوان مثال ، اگر یک میله به طول 8 داشته باشیم و مقادیر فطعات مختلف به صورت زیر براورده شود، حداکثر مقدار قابل دستیابی 22 است (با برش در دو قطعه به طول 6و 2)

    length | 1 2 3 4 5  6  7  8 
    ----------------------------
    price  | 1 5 8 9 10 17 17 20


و اگر قیمت های زیر باشد حداکثر مقدار بدست آمده 24 است ( با برش در 8 قطعه از طول 1 )


    length | 1 2 3 4 5  6  7  8 
    ----------------------------
    price  | 3 5 8 9 10 17 17 20



یک راه حل خیلی ساده لوحانه برای این مشکل تولید تمام تنظیمات قطعات مختلف و یافتن پیکربندی با بالاترین قیمت است. این راه حل از نظر پیچیدگی زمانی نمایی است. بیایید ببینیم که این مسئله چگونه با استفاده از برنامه نویسی پویا قابل حل است  
1. زیر سازی بهینه :<br>
با ایجاد برش در موقعیت های مختلف و مقایسه مقادیر بدست آمده پس از برش، میتوانیم بهترین قیمت را بدست آوریم. ما میتوانیم برای عملکرد قطعه ای که پس از برش بدست آمده است، عملکرد مشابه را فراخوانی کنیم.<br>
را میتوان به صورت زیر نوشت CutRod(n) 
CutRod(n) = max(price [ i ] + CutRod( n - i - 1)) برای همه ارایه ها 
2. زیر پوشش های همپوشانی : <br>
cutrod موارد زیر یک اجرای ساده بازگشتی از مسئله     
<br>

## کد اصلی :
***

```python
# A Naive recursive solution
# for Rod cutting problem
import sys
 
# A utility function to get the
# maximum of two integers
def max(a, b):
    return a if (a > b) else b
     
# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces
def cutRod(price, n):
    if(n <= 0):
        return 0
    max_val = -sys.maxsize-1
     
    # Recursively cut the rod in different pieces 
    # and compare different configurations
    for i in range(0, n):
        max_val = max(max_val, price[i] +
                      cutRod(price, n - i - 1))
    return max_val
 
# Driver code
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", cutRod(arr, size))
 
# This code is contributed by 'Smitha Dinesh Semwal'
```

مشاهده میشود که (برای این مثال کات راد 2 دوبار تکرار میشود)
از انجا که مجددا باید همان مقدار را باید حل کند پس آن را با استفاده از برنامه نویسی پویا optimize میکنیم .
<br>

## شده optimize کد :
***
```python 
# A Dynamic Programming solution for Rod cutting problem
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod(price, n):
	val = [0 for x in range(n+1)]
	val[0] = 0

	# Build the table val[] in bottom up manner and return
	# the last entry from the table
	for i in range(1, n+1):
		max_val = INT_MIN
		for j in range(i):
			max_val = max(max_val, price[j] + val[i-j-1])
		val[i] = max_val

	return val[n]

# Driver program to test above functions
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))

# This code is contributed by Bhavya Jain
```

### output :
    Maximum Obtaiable Value is 22 

