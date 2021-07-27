# portition problem | DP -18


مسئله پارتیشن بندی عناصر موجود در یک آرایه این است که آیا می­توان مجموعه را به دو زیر مجموعه تقسیم کرد به طوری که جمع عدد های موجود در هر کدام از مجموعه با جمع ارایه دیگر برابر باشد.

# : مثال


1. Arr1 = {1, 5, 11, 5}
<br>Output : True
<br>The array can be partitioned as {1, 5, 5} and {11}

</br>

2. Arr2 = {1, 5, 3}<br>
Output : False
<br>The array cannot be partitioned into equal sum sets.
</br>
## : حل مسئله  
***
</br>
 محاسبه مجموع آرایه .اگر جمع فرد باشد ، نمی­توان دو زیر مجموعه با جمع برابر داشت، بنابر این False برگرداند.

اگر جمع عناصر آرایه زوج باشد ، sum/2 را محاسبه کند و زیر مجموعه ای از آرایه را برابر sum/2 پیدا کند .

می­توان آن را با استفاده از برنامه Dynamic Programming یا به صورت بازگشتی حل کرد.

## : شبه کد
***
</br>

      Let isSubsetSum(arr, n, sum/2) be the function that returns true if there is a subset of arr[0..n-1] with sum equal to sum/2

      The isSubsetSum problem can be divided into two subproblems

      IsSubsetSum() without considering last element  
      (reducing n to n-1)

      isSubsetSum considering the last element  
      (reducing sum/2 by arr[n-1] and n to  n-1)

      If any of the above subproblems return true,  then return true.

      isSubsetSum (arr, n, sum/2)  =  isSubsetSum (arr, n-1, sum/2)  ||  isSubsetSum (arr, n-1, sum/2 – arr[n-1])


## : کد اصلی
***
```python

      # A recursive Python3 program for

      # partition problem

      # A utility function that returns

      # true if there is a subset of

      # arr[] with sun equal to given sum

      def isSubsetSum(arr, n, sum):

      # Base Cases

      if sum == 0:

      return True

      if n == 0 and sum != 0:

      return False

      # If last element is greater than sum, then

      # ignore it

      if arr[n-1] > sum:

      return isSubsetSum(arr, n-1, sum)

      ''' else, check if sum can be obtained by any of

      the following

      (a) including the last element

      (b) excluding the last element'''

      return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])

      # Returns true if arr[] can be partitioned in two

      # subsets of equal sum, otherwise false

      def findPartion(arr, n):

      # Calculate sum of the elements in array

      sum = 0

      for i in range(0, n):

      sum += arr[i]

      # If sum is odd, there cannot be two subsets

      # with equal sum

      if sum % 2 != 0:

      return false

      # Find if there is subset with sum equal to

      # half of total sum

      return isSubsetSum(arr, n, sum // 2)

      # Driver code

      arr = [3, 1, 5, 9, 12]

      n = len(arr)

      # Function call

      if findPartion(arr, n) == True:

      print("Can be divided into two subsets of equal sum")

      else:

      print("Can not be divided into two subsets of equal sum")

      # This code is contributed by shreyanshi_arun.
            
```
<br>


## پیچیدگی زمانی : 
***
</br>

در بدترین حالت این راه حل دو احتمال را امتحان میکند.

راه حل Dynamic Programming :

میتوان با استفاده از Dynamic Programming این مشکل را حل کرد که مجموع عناصر خیلی زیاد نباشد.

ما میتوانیم یک آرایه دوبعدی ایجاد کنیم که سایز آن (sum/2 + 1)*(n+1) باشد.
و حل را به روش از پایین به بالا بسازیم به گونه ای که هر ورودی پر شده دارای ویژگی زیر باشد

Part[ i ][ j ] = true if  a  subset of {arr[ 0 ] , arr[ 1 ],  … arr[ j-1 ]} has sum equal to i,  otherwise false

<br>

## : Dynamic Programming استفاده از 
***
<br>

```python
      def  findPartition(arr, n):

      sum = 0

      i, j = 0, 0      

      for  i  in  range(n):

      sum += arr[i]    

      if  sum % 2 != 0:
      return  False     

      part = [[True  for  i  in  range(n + 1)]

      for  j  in  range(sum // 2 + 1)]     

      for  i  in  range(0, n + 1):

      part[0][i] = True     

      for  i  in  range(1, sum // 2 + 1):

      part[i][0] = False
      for  i  in  range(1, sum // 2 + 1):
      for  j  in  range(1, n + 1):

      part[i][j] = part[i][j - 1]
      if  i >= arr[j - 1]:

      part[i][j] = (part[i][j] or

      part[i - arr[j - 1]][j - 1])
      
      return  part[sum // 2][n]
      arr = [3, 1, 1, 2, 2, 1]

      n = len(arr)
      if  findPartition(arr, n) == True:

      print("Can be divided into two",

      "subsets of equal sum")

      else:

      print("Can not be divided into ",

      "two subsets of equal sum")
```

