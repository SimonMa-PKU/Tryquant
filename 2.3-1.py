import numpy as np
# print(np.version.full_version)
a = np.arange(20)
print(a)
print(type(a))
# iterable
b = range(20)
print(b)
print(type(b))
# a = a.reshape(4, 5)
# print(a)
a = a.reshape(2, 2, 5)
print(a)
print(a.ndim)
print(a.size)
print(a.dtype)
print(type(a))

raw = [[range(5), range(5, 10)]]
b = np.array(raw)
print(b)

d = (4, 5)
e = np.zeros(d)
print(e)

f = np.ones(d, dtype= int)
print(f)

print(np.random.rand(5))

a = np.array([[1, 2], [2, 4]])
a = a / 2
print(a)
print(np.exp(a))
print(np.sqrt(a))
print(np.square(a))

a = np.arange(20).reshape(4, 5)
print(a)
print(a.sum())
print(a.max())
# get the max of each row
print(a.max(axis = 1))
# get the min of each col
print(a.min(axis = 0))

a = np.asmatrix(a)
print(a)
print(type(a))
# not recommended
b = np.matrix('1, 2; 3, 4')
print(type(b))

c = np.linspace(0, 3, 10)
print(c)

b = np.arange(15).reshape(5, 3)
b = np.asmatrix(b)
print(a)
print(b)
h = a * b
print(h)
