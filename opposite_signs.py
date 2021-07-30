# Python3 Program to Detect
# if two integers have
# opposite signs.
def oppositeSigns(x, y):
    return ((x ^ y) < 0)

x , y= input("Enter two integer number:").split(' ')

if (oppositeSigns(int(x), int(y)) == True):
    print ("Signs are opposite")
else:
    print("Signs are not opposite")
