A = [1,2,4.9,'hello',67,32,9.7] #create
print(A,type(A))

B = []
print(B,type(B))

C = [5.7]
print(C,type(C))

D = list('hello sir') #type casting
print(D,type(D))

#variable, single variable, multiple variable

print(A)
print(A[1])
print(A[1:6:2])

#update

A[0] = 100
print(A)
A[1:5] = [20,30,40,50,60]
print(A)

#insert
print(A)
A.insert(1,15)
print(A,'/n')

print(A)
del A[0:2]
print(A)
A.pop()
print(A)
A.pop(2)
print(A)
A.remove(30)
print(A)