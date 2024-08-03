import constants
#
# num1 = int(input("enter any number"))
# if num1>0:
#     print("number is positive")
# if num1<0:
#     print("number is negative")
# if num1==0:
#     print("number is zero")
# # #
#
# num2 = int(input("enter any number"))
# if num2>0 or num2==0:
#     print("number is either 0 or positive number")
# else:
#     print("number is negative number")
#
#
# num3 = int(input("enter any number"))
# if num3>0 or num3==0:
#     if num3>0:
#         print("number is positive")
#     else:
#         print("number is zero")
# else:
#     print("number is negative")
#

radius = float(input("Enter the radius of the circle"))
print("1. Calculate the area")
print("2. Calculate the perimeter")
choice=int(input("Enter your choice 1 0r 2"))
if choice == 1:
    print("AREA = ", constants.PI*radius*radius)
else :
    print("PERIMETER = ", 2*constants.PI*radius)
