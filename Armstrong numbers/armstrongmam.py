#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chenn
#
# Created:     27-09-2022
# Copyright:   (c) chenn 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n=int(input("enter a number"))
noofdigits = len(str(n))
var1 = n
sum1 = 0
while var1 >0:
    dig =var1%10
    sum1 =sum1+dig**noofdigits
    var1 =var1//10
if n ==sum1:
    print("yes! armstrong no")
else:
    print("oops! its not a armstrong no")
