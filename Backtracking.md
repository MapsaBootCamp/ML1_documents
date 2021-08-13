<html dir="rtl" lang="fa-IR"></html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="Content-Language" content="fa"> 


# Algorithm
## Backtracking: 
## بازگشت به عقب و یا پساگرد
~~~txt
برگشت به عقب یا پساگرد یک الگوریتم بازگشتی به روش جستجوی عمق اول بین جواب های ممکن است.
~~~
که در این روش هنگام جستجو اگر راهی که طی می‌شود نتیجه نداد( به جواب نرسید) به نقطه‌ی قبلی باز می‌گردد و راه بعدی را انتخاب می‌کند و اگر همه راه‌ها را امتحان کرد و به جواب نرسید جستجو ناموفق بوده است.

این الگوریتم معمولا در قالب توابع بازگشتی پیاده سازی می‌شود، به این صورت که در هر بار فراخوانی تابع، با اضافه شدن یک متغیر به طور متناوب همه مقادیر ممکن را به آن نسبت می‌دهد و آن مقداری که با فراخوانی‌های بازگشتی بعدی سازگار است را ذخیره می‌کند.
___
### **کاربرد‌های الگوریتم بازگشت به عقب**
یکی از استفاده‌های رایج، پساگرد در الگوریتم‌های مسیریاب است که با رفت و برگشت بر روی راس های یک گراف کم هزینه‌ترین مسیر را پیدا می‌کند.استراتژی برگشت به عقب (پساگرد) در پیاده‌سازی زبان‌های برنامه نویسی و چیزهای دیگر مانند تجزیه متن‌ها کاربرد دارد.
___
####  **مسئله‌های برتر آلگوریتم پساگرد:**


* [Hamiltonian Cycle](https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/)

* [Warnsdorff’s algorithm for Knight’s tour problem](https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/)

* [Word Break Problem using Backtracking](https://www.geeksforgeeks.org/word-break-problem-using-backtracking/)

___


### **Sudoku problem**
با توجه به آرایه 2 بعدی 9 × 9 "شبکه [9] [9]" ، هدف این است که ارقام (از 1 تا 9) را به سلولهای خالی اختصاص دهیم تا هر سطر ، ستون و زیر شبکه با اندازه 3 × 3 حاوی دقیقاً یک نمونه از ارقام از 1 تا 9 باشد.

راه حل ساده این است که تمام حالت ممکن را برای حل سودکو در نظر بگیرم و امتحان کنیم. یعنی برای تمام خانه‌های جدول سودوکو باید تمام اعداد یک تا نه را امتحان کنیم و ببینیم آیا سودکو حل شده است یا خیر!

این راه‌حل ساده لوحانه است و مدت زمان زیادی طول می کشد که جواب درست را پیدا 
کنیم.

___

**_آلگوریتم پساگرد در حل مساله سودکو_**

1. تابع‌ای ایجاد کنید که مقادیر صحیح را چک کند و اگر عدد درست بود جواب درست برگداند و اگر اشتباه بود جواب غلط برگرداند
1. در تابع عدد مورد نظر را با اعداد موجود در سطر و ستون و باکس سه در سه چک کنید اگر عددی همانندش نبود این اعداد انتخابی درسا است.

1. اگر در جایی تنها عدد باقی مانده قابل استفاده نبود، ما باید به حالت قبل برگردیم و اعداد دیگری را برای گزینه های قبلی امتحان کنیم.

![Sudoku](https://media.geeksforgeeks.org/wp-content/uploads/sudoku.jpg)

![Sudoku](https://en.wikipedia.org/wiki/File:Sudoku_solved_by_bactracking.gif)

```python

# N is the size of the 2D matrix   N*N
N = 9
 
# A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
 
# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):
   
    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSuduko(grid, row, col):
   
    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
        return True
       
    # Check if column value  becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0
 
    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSuduko(grid, row, col + 1)
    for num in range(1, N + 1, 1):
       
        # Check if it is safe to place
        # the num (1-9)  in the
        # given row ,col  ->we
        # move to next column
        if isSafe(grid, row, col, num):
           
            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            grid[row][col] = num
 
            # Checking for next possibility with next
            # column
            if solveSuduko(grid, row, col + 1):
                return True
 
        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        grid[row][col] = 0
    return False
 
# Driver Code
 
# 0 means unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
 
if (solveSuduko(grid, 0, 0)):
    printing(grid)
else:
    print("no solution  exists ")
 
    # This code is contributed by sudhanshgupta2019a

```
___

## **N-Queen Problem**
داستان از این قرار است که ما به تعداد مشخص  وزیر در صفحه شطرنج خود داریم و می خواهیم آن ها را به شکلی قرار دهیم که هیچ کدام از وزیر‌ها با هم برخورد نکنند.

راه‌حل این است که یک به یک وزیر ها را سطر به سطر یا ستون به ستون قرار دهیم و ببینیم آیا با هم برخورد دارند یا نه، اگر برخورد نداشت مسئله حل میش ود و اگر نه به گزینه قبلی برمی گردیم و مکان بهتری را برای آن پیدا میکنیم.

![N Queen](https://media.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled11-1-e1518086835222.png)

![N Queen](https://media.geeksforgeeks.org/wp-content/cdn-uploads/nQueen-solution2.png)

```python
import time
board = [
        [3, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 2, 5, 0],
        [5, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 7, 9],
        [0, 0, 0, 0, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 7, 0, 0, 4, 5],
        [0, 0, 1, 3, 0, 0, 0, 0, 6]
    ]


def solve(given_board):
    find_valid = find_empty(given_board)

    if not find_valid:
        return True
    else:
        row, column = find_valid

    for i in range(1, 10):
        if find_valid_number(given_board, i, (row, column)):
            given_board[row][column] = i

            if solve(given_board):
                return True

        given_board[row][column] = 0

    return False


def find_valid_number(given_board, number, position):
    # check row
    for i in range(len(given_board)):
        if given_board[position[0]][i] == number and position[1] != i:
            return False

    # check column
    for i in range(len(given_board)):
        if given_board[i][position[1]] == number and position[0] != i:
            return False

    # check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if given_board[i][j] == number and (i, j) != position:
                return False

    return True


def print_board(given_board: list[list]):
    for i in range(len(given_board)):

        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(given_board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(given_board[i][j])
            else:
                print(str(given_board[i][j]) + " ", end="")


def find_empty(given_board: list[list]):
    for i in range(len(given_board)):
        for j in range(len(given_board[0])):
            if given_board[i][j] == 0:
                return i, j

    return None


print("Not solved Sudoku Table: ")
print_board(board)
print()
print()
print("solved sudoku table:")
start_time = time.time()
solve(board)
print("--- %s seconds ---" % (time.time() - start_time))
print_board(board)



```