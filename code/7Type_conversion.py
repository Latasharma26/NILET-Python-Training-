# # IMPLICIT_CONVERSION
# integer_number = 123
# float_number = 1.23
# new = integer_number + float_number
# print("Value:",new)
# print("Data Type:",type(new))
# #
# EXPLICIT CONVERSION
num_s = '12'
num_i = 23
print("Data type of num_string before Type Casting:",type(num_s))
num_s = int(num_s)
print("Data type of num_string after Type Casting:",type(num_s))
sum = num_i + num_s
print("Sum:",sum)
print("Data type of sum:",type(sum))

# # int() float() str() bool()