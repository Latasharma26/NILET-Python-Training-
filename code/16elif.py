import constants
#
# num1=int(input("Enter any number"))
# if num1>0:
#     print("number is positive")
# elif num1==0:
#     print("number is zero")
# else :
#     print("number is negative")

# WAP to find smallest of 3 numbers

radius = float(input("enter radius:"))
choice = int(input("enter your choice\n"
                   "1. AREA OF CIRCLE \n"
                   "2. Area of sphere\n"
                   "3. Area of hemisphere \n"))
if choice == 1:
    print("AREA OF CIRCLE:\n",constants.PI*radius*radius)
elif choice == 2:
    print("Area of sphere :\n", 4/3*constants.PI*radius*radius)
elif choice == 3:
    print("Area of hemisphere :\n", 2/3*constants.PI*radius*radius)
else :
    print("invalid choice")
# # program to do = WAP for calculator
