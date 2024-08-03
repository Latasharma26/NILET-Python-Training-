# # dynamic typing
# vars = 'HELLO WORLD'
# print(vars)
# print(type(vars))
#
# vars = 1967
# print(vars)
# print(type(vars))

# multiple assignment
a=b=c=100
print(a, b, c)

# multiple values
x, y, z=10, 20, 30
print(x, y, z)

# swapping
num1, num2=25, 50
num1, num2=num2, num1

# Expression assignment
p, q, r=5, 10, 7
q, r, p=p + 1, q + 2, r - 1
print(p, q, r)

# l_value and r_value
x=10
y, y=x + 2, x + 5
print(x, y)
