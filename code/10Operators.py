# Relational Operators (<,>,<=,>=,=,==,!=)
# output is always boolean
# import constants
# print(constants.PI)

#
# # numeric relational
# print(4 == 4.0)
# print(4.000012412 == 4)
# print(4.2 == 4)
# print(4 > 4.0)
# print(4 < 4.0)
# print(4 >= 4.0)
# print(4 <= 4.0)
# print(123 != 123.009)

# String relational (Lexicographical)
# a(97)>A(65)
print('Apple' > 'apple')
print('Apple' > ' apple')
print('Apple' == 'Apple ')

# List, Dictionary and tuple (same order,position)
L1 = [1, 2, 3]
L2 = [1, 2, 3, 4]
L3 = [1, 2, 3]
print(L1 == L2, L1 == L3)

# precedence
a, b = 3, 2
print(a + 5 > b- 2)
