class CanFly:
    def fly(self):
        print('I beleave I can fly')


class Animal:
    voice = 'I don`t know what to say'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def golos(self):
        print(self.voice)


class Dog(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.voice = 'Gav Gav'


class Cat(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.voice = 'Meow Meow'


class Lizard(Animal):
    pass


class Bird(Animal, CanFly):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.voice = 'Krya'


lizard = Lizard(1, 'yasha')
lizard.golos()
cat = Cat(3, 'Murzik')
cat.golos()
dog = Dog(5, 'Bobik')
dog.golos()
bird = Bird(1, 'Duffy')
bird.golos()
bird.fly()


# Роздрукувати значення атрибуту age класу Animal
# print(Animal.age)

# cat1 = Animal(age=2, name='Murzik', family='cat')
# cat2 = Animal(age=5, name='Rudyy', family='cat')
# dog1 = Animal(age=3, name='Bobik', family='dog')


class A:
    value = 1


class B(A):
    pass


class C(B):
    def __init__(self):
        value = 3


class D(C):
    def __init__(self):
        self.value = 4


A.value  # 1
B.value  # 1
C.value  # 1
D.value  # 1

A().value  # 1
B().value  # 1
C().value  # 1
D().value  # 4


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        if self.gender == 'f':
            if self.age < 23:
                x = 'girl'
            else:
                x = 'woman'
        else:
            if self.age < 23:
                x = 'boy'
            else:
                x = 'man'
        print(f'hello, my name is {self.name} and I am {x}')


masha = Human('Masha', 19, 'f')
masha.greet()

svitlana = Human('Svitlana', 25, 'f')
svitlana.greet()
kolya = Human('Kolya', 19, 'm')
vasyl = Human('Vasyl', 26, 'm')

kolya.greet()
vasyl.greet()
