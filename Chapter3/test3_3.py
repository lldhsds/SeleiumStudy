# 函数简单实例
def hello(name):
    """Print Hello + name"""
    print("Hello {}".format(name))

if __name__ == '__main__':
    hello('Storm')

# 函数参数-位置参数，计算x的n次幂
def power(x, n):
    '''定义一个函数，计算x的n次放'''
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

if __name__ == '__main__':
    print(power(3,2))
    print(power(2,3))


# 函数参数-默认参数，默认计算x的平方
def power(x, n=2):
    '''定义一个函数，计算x的n次放'''
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

if __name__ == '__main__':
    print(power(3))
    print(power(2))

# 函数参数-可变参数。在函数调用时会自动组装为一个元组。*args是可变参数，args接收的是一个元组。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

if __name__ == '__main__':
    print(calc(1,2,3))

# 函数参数-关键字参数。关键字参数允许传入0个或任意多个含参数名的参数，参数会在函数内部会自动组装为一个字典。**kw是关键字参数，kw接收的是一个字典。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person("Storm", 30)
person('SK', 35, city='Beijing')
person('UG', 45, gender='M', job='Engineer')

# 函数参数-命名关键字参数。对传入的关键字参数在函数内部通过kw检查。
def person(name, age, **kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)