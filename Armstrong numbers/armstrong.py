#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chenn
#
# Created:     26-09-2022
# Copyright:   (c) chenn 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n=str(input("enter number"))
a =len(str(n))
sum = 0
for i in range(0,a):
    k = 1
    x = int(n[i])
    for c in range(0,a):
        k = k*x
    sum = sum+k
if(sum==int(n)):
        print(n,"is armstrong")
else:
    print(n,"is not armstrong")
