x = {1:'hello',2:'hi',3:'bye'}

y = {a:b.upper() for a,b in x.items() if b=='hi'}
print(y)