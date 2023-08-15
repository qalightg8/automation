class Human:
    favorite_drink = 'beer'

    def __init__(self, age: int):
        self.age = age
        if self.age < 18:
            self.favorite_drink = 'juice'

    def drink(self):
        print(f'I am {self.__class__.__name__} {self.age}'
              f' years old and I like to drink {self.favorite_drink}')


class Worker(Human):

    def __init__(self, age, salary):
        super().__init__(age)
        self.salary = salary
        if self.age > 18 and self.salary > 1000:
            self.favorite_drink = 'whiskey'


human1 = Human(19)
human1.drink()

human2 = Human(15)
human2.drink()

worker1 = Worker(15, 2000)
worker1.drink()

worker2 = Worker(20, 2000)
worker2.drink()

worker3 = Worker(30, 1000)
worker3.drink()
