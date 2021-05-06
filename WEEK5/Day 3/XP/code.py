# http://learn.di-learning.com/courses/collection/18/course/13/section/63/chapter/328

# Exercise 1 : Built-In Functions

# class Value:

#     def abs():
#         x = abs(-200200)
#         return x


# print(Value.__doc__)


# class Test():

#     def int():
#         x = int(3.5)


# test(Test.__doc__)


# Exercise 2: Currencies
class Currency():
    def __init__(self, coin_type, amount):
        self.coin_type = coin_type
        self.amount = amount

    def __repr__(self):
        return f'{self.coin_type} {self.amount}'

    def __str__(self):
        return f'{self.coin_type} {self.amount}'

    def __int__(self):
        return f'{self.coin_type} {self.amount}'


c1 = Currency('dollar', 5)
c3 = Currency('shekel', 10)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)

int(c1)
c4
