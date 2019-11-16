
def square(x):
    return x * x

print(square(99))


t = 2
if t == 3:
    print('t=3')
elif t < 3:
    print('t<3')
else:
    print('t>3')

a = 3
while a < 10:
    a += 1
    print(a)
    if a == 9:
        break

b = range(10)
for i in b:
    print(i)

print([x * x for x in range(4)])
print([x * x for x in range(10) if x % 3 ==0])

class boy:
    gender = 'male'
    interest = 'female'
    def say(self):
        return 'I am a boy~'
peter = boy()
peter.gender
print(peter.interest)
peter.say()
print(peter.say())