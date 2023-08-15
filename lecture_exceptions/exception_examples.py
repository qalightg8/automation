a = 2
b = 0


# print(a / b)


class MyOwnException(Exception):
    pass


class MyClass:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a/b

    def other1(self):
        raise TypeError('Type error message here')

x = MyClass()
print(x.add(1, 2))

try:
    x.div(5, 1)
    x.other1()
except NotImplementedError:
    print('function "div" not implemented yet, but no worry, all will be OK')
except Exception as exc:
    print(exc)
    print(f'Тут було якесь виключення: {exc.__class__}')
else:
    print(x.div(5, 0))
finally:
    print('I am always here')
