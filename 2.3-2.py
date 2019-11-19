import numpy as np
import numpy.linalg as nlg

a = np.array([[1, 2], [3, 4]])
# shift + Enter: quick to the next line
# a[raw][col]
print(a[0][1])
print(a[0, 1])
# change a and b at the same time
b = a
a[0][1] = 9
print(a)
print(b)
# only change a
b = a.copy()
a[0, 1] = 0
print(a)
print(b)

a = np.arange(20).reshape(4, 5)
print(a)
print("the 2nd and 4th column of a: ")
print(a[:, [1, 3]])
# print the 3rd col array corresponding to the 2nd col number bigger than 1;
print(a[:, 2][a[:, 1] > 1])
# a is an array, using transpose
a = np.random.rand(2, 4)
print(a.transpose())
print(a)
# b is a matrix, using b.T
b = np.random.rand(2, 4)
b = np.mat(b)
print(b.T)

b = np.random.rand(2, 2)
# change b to matrix, for the right inverse
b = np.mat(b)
ib = nlg.inv(b)
print("b: ")
print(b)
print("the inverse of b: ")
print(ib)
print('b * inv(b)')
print(b * ib)

a = np.random.rand(3, 3)
eig_value, eig_vector = nlg.eig(a)
print('eigen value: ')
print(eig_value)
print('eigen vector: ')
print(eig_vector)

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(np.column_stack((a, b)))

a = np.random.rand(2, 2)
b = np.random.rand(2, 2)
print('a: ')
print(a)
print('b: ')
print(b)
c = np.hstack((a, b))
d = np.vstack((a, b))
print('horizontal stacking: ')
print(c)
print('vertical stacking: ')
print(d)

a = np.random.rand(2, 2)
a[0, 1] = np.nan
print(np.isnan(a))

print(np.nan_to_num(a))
