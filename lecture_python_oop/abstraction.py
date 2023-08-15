import abc
from abc import abstractmethod


class Human(abc.ABC):

    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class Worker(Human):
    def talk(self):
        print(f'{self.__class__.__name__} can talk')

    def walk(self):
        pass


w1 = Worker()
w1.talk()

private
public
protected