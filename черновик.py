a=[1, 22, 3]
b=tuple(a)
print(a)
print((b))
a[1]=4
print(a)
c=b+tuple(a)
print(c)