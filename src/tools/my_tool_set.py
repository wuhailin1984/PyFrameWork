import math
import os

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def movement(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if (delta < 0):
        return 'no solutions'
    if (delta == 0):
        return -b / (2 * a)
    else:
        tmp = math.sqrt(delta)
        return ((-b + tmp) / (2 * a), (-b - tmp) / (2 * a))


def calc_sum(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def calc_sum_variable_parameters(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def person(name, age, **kw):
    if 'city' in kw:
        print('city exists')
    if 'job' in kw:
        ('job exists')
    print('name:', name, 'age:', age, 'other:', kw)


def person_check_parameters(name, age, *, city, job):
    print(name, age, city, job)


def person_combined(name, age, *args, city, job):
    print(name, age, args, city, job)


def fact(num):
    if num == 1:
        return num
    return num + fact(num - 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num + product)


def move(n, a, b, c):
    if n == 1:
        print(a + '  to  ' + c)
        return
    move(n - 1, a, c, b)
    print(a + '  to  ' + c)
    move(n - 1, b, a, c)
    return


def build_a_list(length, first_value, step_value):
    l = []
    if (isinstance(length, int)) and (length >= 0):
        for i in range(length):
            l.append(first_value + step_value * i)
    return l

def trim(s):
    if isinstance(s,str):
        i=0
        length=len(s)
        for i in range(length):
            if s[i]==' ':
                pass
            else :
                break
        j=0
        for j in range(length):
            if s[length-j-1]==' ':
                pass
            else :
                break
        return s[i:length-j]


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

"""
print(my_abs(12))
print(movement(0, 0, 10, 30))
print(quadratic(2, -2, 1))
print(calc_sum([1, 2, 3]))
print(calc_sum_variable_parameters(1, 2, 3, 4))
aList = [1, 2, 3]
print(calc_sum_variable_parameters(*aList))
person('a_name', 30)
person('a_name', 30, dep='IT', salary=20)
a_dict = {'dep': 'RD', 'salary': 200}
person('Lily', 28, **a_dict)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)
person_check_parameters('Peter', 30, city='Stockholm', job='tester')
# person_check_parameters('Bob', 30, dep='IT', salary=20)
person_combined('Peter', 30, 1, 2, 3, city='Stockholm', job='tester')

print(fact(10))
print(fact_iter(10, 1))
# print(fact_iter(1000,1))
# print(fact(1000))

move(3, 'A', 'B', 'C')
print(build_a_list(3, 0, 1))
print(build_a_list(3, 0, 2))
print(build_a_list(3, 0, 2)[:2])
print(build_a_list(3.9, 0, 1))

L = list(range(100))
print(L)
print( L[:10:2])
print( L[:11:2])
print( L[::10])
print( L[:])

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('test failed')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('test failed')
else:
    print('test successed')

print( trim('  hello  '))
print( trim('  hello world  '))
"""

L1=list(x * x for x in range(1, 11))
print(L1)
print( [m + n for m in 'ABC' for n in 'XYZ'])
print( [d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

L2 = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L2])

L1=['Hello','World',18,'Apple',None]
L2=[i.lower() for i in L1 if isinstance(i,str)]
print(L2)

L3=[x.lower() if isinstance(x,str) else x for x in L1]
print(L3)


f=lambda n:(n%2==1)
L = list(filter(f, range(1, 20)))
print(L)
