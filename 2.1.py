from math import sqrt

a = 1+3*3
print(a)


print(sqrt(9))
a = [1, 3, 6, 10]
print(a[2])

b = (1, 3, 6, 10)
print(b[2])

c = 'hello'
print(c[1:3])

d = {7:'seven', 8:'eight', 9:'nine'}
print(d[8])

print(a[3])
print(a[-1])

print('hello,'+'world')
print('o' in 'hello')

print(list('hello'))

e = list('hello')
e[2] = 't'
print(e)
e[2:4] = list('yy')
print(e)
e.insert(2, 't')
print(e)
e.append('q')
print(e)
print(e.index('e'))
e.remove('e')
print(e)
e.sort()
print(e)

f = {'age': 27, 'name': 'Simon'}
print(len(f))
print(f['age'])
f['age'] = 28
print(f)
del f['name']
print('age' in f)