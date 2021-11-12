A = {'a':10,'b':20,'c':30}
print(A,type(A))

B = {}
print(B,type(B))

print('\n',A.keys(),A.values(),A.items())

print(A)
del A['b']
print(A)
A.popitem()
print(A)

