# type_infered language
# variable is not created until some value is assigned to it
# In traditional programming location didn't changed but only its content changed age=15 , age=20

# In python
A_var = 15
# print(type(A_var))
print(id(A_var))

B_var = 15
print(id(B_var))

p = 5
q = p
r = 5
print(id(p))
print(id(q))
print(id(r))

