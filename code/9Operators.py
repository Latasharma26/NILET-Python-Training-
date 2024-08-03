# # ARITHMETIC OPERATORS (+,-,/,%,*,//,**)
# print(bool(0))
# print(bool(str(0)))
# print(2+3)
# print(2-3)
# print(2%3)
# print(2/3)
# print(2//3)  #floor division
# print(2*3)
# print(2**3)   #exponential

# Shortcut operations (+=,-=,/=,%=,*=,//=,**=)
# a =3
# a+=10
# print(a)  #a=a+10
# a = 1 + (3 + 5j)
# print(type(a), a)  # int+complex = complex
# b = 2 + 2.3
# print(type(b), b)  # int+float = float
# c = 4.55 + (8 + 3j)
# print(type(c), c)  # float+complex = complex
#
# a = True + True
# b = True + False
# c = False + False
# print(a, b, c)
# print("hello" + 2)

a = bool(0)
print(a == False)
b = bool(1)
print(b == False)


str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)
