class Human:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def print_full_name(self):
        print(self.fname + ' ' + self.lname)


class A:
    def func_1(self):
        print('func_1')
        return self

    def func_2(self):
        print('func_2')
        return Human('Vasya', 'Pupkin')


A().func_1().func_1().func_2().print_full_name()
