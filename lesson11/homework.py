"""
1.
Напишите итератор Fibonacci(n), который генерирует числа Фибоначчи до
n включительно.
"""
class Fibonacci:
    def __init__(self, number):
        self.number = number
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.first
        if fib > self.number:
            raise StopIteration
        self.first, self.second = self.second, self.first + self.second
        return fib


"""
2.
Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.
"""
class Even:
    def __init__(self, number):
        self.number = number
        self.first = 0

    def __iter__(self):
        return self

    def __next__(self):
        even = self.first
        if even > self.number:
            raise StopIteration
        self.first += 2
        return even


"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


"""
4.*
Напишите итератор BinomialCoefficients(n), генерирующий последовательность
биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""
