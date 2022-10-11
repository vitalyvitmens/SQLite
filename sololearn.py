# my_boolean = True
# print(my_boolean)
# # True
#
# print(2 == 3)
# # False
#
# print("hello" == "hello")
# # True
#
# x = 7
#
# print(x != 8)
# print(x > 5)
# print(x < 2)
# print(x >= 7)
# print(x <= 7)
#
# print('a' > 'b')
# print("Bob" > "Dave")
#
# print('hey' < 'hay')
#
# x = (7 > 5)
# print(int(x))
#
# x = 42
# if x > 5:
#     print("x is greater than 5")
# spam = 7
#
# if spam > 5:
#     print("five")
#
# if spam > 8:
#     print("eight")
#
# age = 24
#
# if age > 18:
#     print("Cool")
#
# num = 12
# if num > 5:
#     print("Bigger than 5")
#     if num <= 47:
#         print("Between 5 and 47")
#
# num = 7
#
# if num > 3:
#
#     print("3")
#
#     if num < 5:
#
#         print("5")
#
#         if num == 7:
#             print("7")
# temp = int(input())
# if temp >= 100:
#     print('Boiling')

# x = 'a'
#
# if (x < 'c'):
#     print(x < 'c')
#     x += 'b'
#
# if (x > 'z'):
#     print(x > 'z')
#     x += 'c'
#
# print(x)
# print(x, 'z')
# print(x > 'z')

# x = 4
# if x == 5:
#     print("Yes")
# else:
#     print("No")
#
# if 1 + 1 == 2:
#     if 2 * 2 == 8:
#         print("if")
#     else:
#         print("else")

# num = 3
# if num == 1:
#     print("One")
# else:
#     if num == 2:
#         print("Two")
#     else:
#         if num == 3:
#             print("Three")
#         else:
#             print("Something else")
#
# num = 3
# if num == 1:
#     print("One")
# elif num == 2:
#     print("Two")
# elif num == 3:
#     print("Three")
# else:
#     print("Something else")
#
# num = 8
# if num == 1:
#     print("One")
# elif num == 2:
#     print("Two")
# elif num == 3:
#     print("Three")
# else:
#     print("Something else")
#
# age = int(input())
# if age >= 18:
#     print('Allowed')
# else:
#     print('Sorry')
#
# x = 10
# y = 20
# if x > y:
#     print(x + y)
# else:
#     print(y - x)
# hour = 20
# day = "Sunday"
# if hour > 20 or day == "Sunday":
#     print("Closed")
# else:
#     print("Open")
#
# print(not 1 == 1)
# # False
# print(not 1 > 7)
# # True
# if not True:
#     print("1")
# elif not (1 + 1 == 3):
#     print("2")
# else:
#     print("3")
#
# country = "US"
# age = 42
#
# if (country == "US" or country == "GB") and (0 < age < 100):
#     print("Cool")
# hour = 9
# day = 23
# print((hour > 12 and day <= 15) or (hour < 10))

"""
Порядок операций в Python такой же, как и в обычной математике: 
сначала круглые скобки, затем возведение в степень, 
затем умножение/деление, а затем сложение/вычитание.
() ** * / + - 
"""

# import readline

# age = int(input())
# if 0 <= age <= 11:
#     print('Child')
# elif 12 <= age <= 17:
#     print('Teen')
# elif 18 <= age <= 64:
#     print('Adult')
# else:
#     print('Something else')

# TODO: Цикл while полезен в тех случаях, когда количество итераций неизвестно и
#  зависит от некоторых вычислений и условий в кодовом блоке цикла.
#  Например, завершение цикла, когда пользователь вводит определенный ввод в программе-калькуляторе.
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
#
# print("Finished!")
#
# x = 0
# while x < 10:
#     print(x)
#     x += 1

# sum = 0
# x = 10
# while x > 0:
#     print(x)
#     sum += x
#     x -= 1
#
# print(f'\n{sum}')

# sum = 0
# x = 0
# while x <= 10:
#     print(x)
#     sum += x
#     x += 1
# x = 10
# while x >= 0:
#     print(x)
#     sum += x
#     x -= 1
#
# print(f'\n{sum}')
#
# i = 3
#
# while i >= 0:
#     print(i)
#     i = i - 1

# x = 1
# while x <= 10:
#     if x % 2 == 0:
#         print(f'{str(x)} is even')
#     else:
#         print(f'{str(x)} is odd')
#
#     x += 1

# x = 8
# while x > 3:
#     print(x)

# x = 1
# while x == 1:
#     print("In the loop")

# x = 0
# while x <= 10:
#     if x % 2 == 0:
#         print(x)
#     x += 1

# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if i >= 5:
#         print("Breaking")
#         break
#
# print("Finished")

# i = 5
# while True:
#     print(i)
#     i = i - 1
#     if i <= 2:
#         break

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         print("Skipping 3")
#         continue
#     print(i)

# i = 0
# while True:
#     i += 1
#     if i == 2:
#         continue
#     if i == 5:
#         break
#     print(i)

# total = 0
# i = 0
# while i < 5:
#     age = int(input())
#     i += 1
#     if age < 3:
#         continue
#     total += 100
#
# print(total)

# i = 0
# x = 0
# while i < 4:
#     x += i
#     print(i)   # вывод в консоль каждой итерации
#     i += 1
# print(x)   # сумма итераций
# print(i)   # количество итераций

# x = int(input())
# if x > 5:
#     if x < 8:
#         print(x + 1)
#     else:
#         print(x - 1)
# else:
#     print(x)

# weight = int(input())
# height = float(input())
# BMI = weight / (height * height)
# if 0 <= BMI < 18.5:
#     print('Underweight')
# elif 18.5 <= BMI < 25:
#     print('Normal')
# elif 25 <= BMI < 30:
#     print('Overweight')
# else:
#     print('Obesity')

# TODO: списки
# words = ["Hello", "world", "!"]
# print(words[0], end=' ')
# print(words[1], end='')
# print(words[2])

# x = ["a", "b", "c"]
# y = [1, 2, 3, 4, 5]
# print(x[1])
# print(y[3])

# m = [
#     [1, 2, 3],
#     [4, 5, 6]
#     ]

# m = [
#     [1, 2, 3],
#     [4, 5, 6]
#     ]
#
# print(m[1][2])

# things = ["text",
#           0,
#           [1, 2, 8],
#           4.56]
# print(things[2][2])

# str = "Hello world!"
# print(str[6])

# x = "Python"
# print(x[1] + x[4])

# string = str(input())
# print(string[2])

# nums = [5, 8, 2]
# nums[1] = 42
# print(nums)

# nums = [1, 2, 3, 4, 5]
# nums[3] = nums[1]
# print(nums[3])
# print(nums)

# nums = [1, 2, 3]
# print(nums + [4, 5, 6])

# x = [2, 4]
# x += [6, 8]
# print(x[2]//x[0])

# nums = [1, 2, 3]
# print(nums * 3)

# x = [2, 4]
# x = x * 3
# print(x[3])

# words = ["spam", "egg", "spam", "sausage"]
# print("spam" in words)
# print("egg" in words)
# print("tomato" in words)

# nums = [10, 9, 8, 7, 6, 5]
# nums[0] = nums[1] - 5
# if 4 in nums:
#     print(nums[3])
# else:
#     print(nums[4])
# print(nums)

# x = "hello world"
# if "world" in x:
#     print("Yes")

# nums = [1, 2, 3]
# print(not 4 in nums)
# print(4 not in nums)
# print(not 3 in nums)
# print(3 not in nums)

# x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
# num = int(input())
# if num in x:
#     print('bingo')
# else:
#     pass

# TODO: Цикл for используется для перебора заданной последовательности, такой как списки или строки.
# words = ["hello", "world", "spam", "eggs"]
# for word in words:
#     print(word + "!")

# nums = [4, 7, 3, 1]
# for x in nums:
#     print(x * 2)

# string = "testing for loops"
# count = 0
# for x in string:
#     if x == 't':
#         count += 1
# print(count)

# text = "some text"
# for x in text:
#     if x == 'e':
#         continue
#     if x == 'x':
#         break
#     print(x)

# lists = [2, 3, 4, 5, 6, 7]
# for x in lists:
#     if x % 2 == 1 and x > 4:
#         print(x)
#         break

# x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
# count = 0
# for num in x:
#     count += num
# print(count)

# nums = [1, 2, 3, 4]
# res = 0
# for x in nums:
#     if x % 2 == 0:
#         continue
#     else:
#         res += x
# print(res)

# TODO: Range позволяет очень легко создавать числовые последовательности
# numbers = list(range(10))
# print(numbers)

# for i in range(5):
#     print("hello!")

# nums = list(range(5))
# print(nums)
# print(nums[4])

# numbers = list(range(3, 8))
# print(numbers)

# print(range(20) == range(0, 20))

# numbers = list(range(5, 20, 2))
# print(numbers)

# nums = list(range(3, 15, 3))
# print(nums[2])

# x = list(range(7, 3, -1))
# print(x)

# x = list(range(7, 3, -1))
# print(x)

# numbers = list(range(5, 10, 2))
# print(numbers)

# a = int(input())
# b = int(input())
# print(list(range(a, b)))

# TODO: List Slices позволяют получить часть списка, используя два индекса, разделенных двоеточиями.
#  Это возвращает новый список, содержащий все значения между индексами.
# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[2:6])
# print(squares[3:8])
# print(squares[0:1])

# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[:7])
# print(squares[7:])
# print(squares[::2])
# print(squares[1:-1])
# print(squares[::-1])
# print(squares[2:8:3])
# print(squares[1::4])
# print(squares[7:5:-1])

# nums = [1, 2, 3, 4, 5, 6]
# res = nums[::-1]
# print(res[2])

# a = input()
# print(a[-1])

# x = input()
# elements = x.split()
# print(elements[-1])

# names = [1, 2, 3, 4, 5]
# print(names[1:-1])

# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])

# for i in range(10):
#     if not i % 2 == 0:
#         print(i + 1)

# N = int(input())
# count = 0
# for i in (range(0, N+1)):
#     count += i
# print(count)

#  TODO: List Comprehensions Генерация списков — удобный способ быстрого создания списков,
#   содержимое которых подчиняется простому правилу.
# a list comprehension:
# cubes = [i ** 3 for i in range(10)]
# print(cubes)

# nums = [i * 2 for i in range(10)]
# print(nums)

# evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
# evens2 = [i ** 2 for i in range(10) if i ** 2 % 2 == 1]
# print(evens)
# print(evens2)

# a = [i for i in range(20) if i % 3 == 0]
# print(a)

# a = [x * 10 for x in range(5, 9)]
# print(a)

# # Попытка создать список в очень широком диапазоне приведет к ошибке MemoryError .
# # В этом коде показан пример, когда для понимания списка не хватает памяти.
# # Эту проблему решают генераторы , которые рассматриваются в следующем модуле.
# even = [2 * i for i in range(10 ** 100)]

# x = int(input())
# evens = [i for i in range(x) if i % 3 == 0 and i % 5 == 0]
# print(evens)

# TODO: Functions — это группа связанных операторов, которая выполняет определенную задачу.
#  Пример функции: print("Hello"), где print — это имя функции, а «Hello» — аргумент.
# print("Hello world!")
# range(2, 20)
# str(12)
# range(10, 20, 3)

# nums = [1, 3, 5, 2, 4]
# print(len(nums))

# letters = ["a", "b", "c"]
# letters += ["d"]
# print(len(letters))

# str = "some text"
# x = len(str)
# print(x)

# nums = [1, 2, 3]
# nums.append(4)
# print(nums)

# words = ["Python", "fun"]
# words.insert(1, "is")
# print(words)

# nums = [9, 8, 7, 6, 5]
# nums.append(4)
# nums.insert(2, 11)
# print(len(nums))

# letters = ['p', 'q', 'r', 's', 'p', 'u']
# print(letters.index('r'))
# print(letters.index('p'))
# print(letters.index('q'))

# x = [1, 8, 42, 3]
# print(min(x))
# print(max(x))

# nums = [1, 3, 5, 2, 4]
# res = min(nums) + max(nums)
# print(res)

# list = [8, 4, 2, 6]
# list.remove(2)
# print(len(list)+list.count(6))

# queue = ['John', 'Amy', 'Bob', 'Adam']
# x = input()
# queue.append(x)
# print(queue)

# nums = [2, 4, 8, 9, 5]
# print(nums)
# nums.insert(1, 3)
# print(nums)
# nums.remove(9)
# print(nums)
# nums.insert(0, nums.count(8))
# print(nums)
# print(nums[3])

# nums = [4, 5, 6]
# msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
# nms = f"Numbers: {nums[0]} {nums[1]} {nums[2]}"
# print(msg)
# print(nms)

# print("{0}{1}{0}".format("abra", "cad"))

# a = "{x}, {y}".format(x=5, y=12)
# print(a)

# x = ", ".join(["spam", "eggs", "ham"])
# print(x)

# string = "some text goes here"
# x = string.split(' ')
# print(x)

# x = 'Чудук Виничук'
# words = x.split(' ')
# res = words[1]
# print(res)
# print(words)

# x = "Hello ME"
# print(x.replace("ME", "world"))

# x = 'Семенович Игорь '
# print(x.replace('Семенович', 'Чудук'))

# print("This is a sentence.".upper())
# print("AN ALL CAPS SENTENCE".lower() + ".")

# msg = input()
# print(msg.replace('#', ' '))

# txt = "hello"
# print(max(txt))

# latin = "abcdefghijklmnopqrstuvwxyz"
# count = 0
# list_dic = []
# for i in range(0, 26):
#     count += 1
#     dic = {latin[i], count}
#     list_dic.append(dic)
# print(list_dic)
# print(latin.index('o') + 1)


# def my_func():
#     print("spam")
#     print("spam")
#     print("spam")


# def hello():
#     print("Hello world!")

# def welcome():
#     print(f"Welcome, {user}")
#
#
# user = input()
# welcome()

# def exclamation(word):
#     print(word + "!")
#
#
# exclamation("spam")

# def print_sum_twice(x, y):
#     print(x + y)
#     print(x + y)
#
#
# print_sum_twice(5, 8)

# def printBill(text):
#     print("======")
#     print(text)
#     print("======")
#
#
# text = input()
# printBill(text)

# def msg(num, ch):
#     print(ch + str(num))
#
#
# msg(18, 'A')

# def sum(x, y):
#     return x + y
#
#
# a = sum(4, 6)
# print(a)

# def sum(x, y):
#     return x + y
#
#
# res = sum(42, 7)
# print(res)

# def max(x, y):
#     if x >= y:
#         return x
#     else:
#         return y
#
#
# if max(6, 4) > 10:
#     print("Yes")
# else:
#     print("Nope")
# print(max(6, 4))

# def add_numbers(x, y):
#     total = x + y
#     print("Это будет напечатано!")
#     return total
#     print("Это не будет напечатано!")
#
#
# print(add_numbers(4, 5))

# def double(a, b):
#     return [a * 2, b * 2]
#
#
# x = double(6, 9)
# print(x)

# def area(x, y):
#     print(x * y)
#
#
# w = int(input())
# h = int(input())
#
# area(w, h)


# def sum(x):
#     res = 0
#     for i in range(x):
#         res += i
#         print(res)
#     return res
#
#
# print(f'\n{sum(4)}')

# x = 365
# y = 7
# print(x % y)  # find the remainder

# x = 365
# y = 7
# # this is a comment
#
# print(x % y)  # find the remainder


# print (x // y)
# another comment

# def shout(word):
#     """
#     Print a word with an
#     exclamation mark following it.
#     """
#     print(word + "!")
#
#
# shout("spam")

# def print_nums(x):
#     for i in range(x):
#         print(i)
#         return
#
#
# print_nums(10)

# def func(x):
#     res = 0
#     for i in range(x):
#         res += i
#     return res
#
#
# print(func(3))

# def search(a, b):
#     if b in a:
#         return "Word found"
#     return "Word not found"
#
#
# text = input()
# word = input()
#
# print(search(text, word))

# print(8 ** (1 / 3))
# print(1000 // 1.6)
# print(1000 / 1.6)
# print(20 % 6)
# print(1.25 % 0.5)
# print(7 % (5 // 2))
# print((3 ** 2) // 2)
# print('A\nB\nC\nD')
# print("ni" * 3 + "!")

# x = input()
# y = int(input())
# print(x * y)

# print(num := int(input()))

# x = 5
# y = x + 3
# y = int(str(y) + "2")
# print(y)

# print(7 > 7.0)

# num = 7
# if num > 3:
#     print("3")
#     if num < 5:
#         print("5")
#         if num == 7:
#             print("7")

# temp = int(input())
# if temp >= 100:
#     print('Boiling')

# if 1 + 1 == 2:
#     if 2 * 2 == 8:
#         print("if")
#     else:
#         print("else")

# if not True:
#     print("1")
# elif not (1 + 1 == 3):
#     print("2")
# else:
#     print("3")

# age = int(input())
# name = input()
# if 18 <= age:
#     print(f'Welcome {name}')
# else:
#     print('Sorry')

# if 1 + 1 * 3 == 6:
#     print("Yes")
# else:
#     print("No")

# x = 4
# y = 2
# if not 1 + 1 == y or x == 4 and 7 == 8:
#     print("Yes")
# elif x > y:
#     print("No")

# type = input()
# if type == 'Visa' or type == 'Amex':
#     print('accepted')

# TODO: List
# number = 3
# things = ["string",
#           0,
#           [1, 2, number],
#           4.56]
# print(things[1])
# print(things[2])
# print(things[2][2])

# m = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(m[1][2])

# fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
# num = int(input())
# if 0 <= num <= 7:
#     print(fruits[num])
# else:
#     print('Wrong number')

# words = ["spam", "egg", "spam", "sausage"]
# print("spam" in words)
# print("egg" in words)
# print("tomato" in words)

# nums = [10, 9, 8, 7, 6, 5]
# nums[0] = nums[1] - 5
# if 4 in nums:
#     print(nums[3])
# else:
#     print(nums[4])

# nums = [1, 2, 3]
# print(not 4 in nums)
# print(4 not in nums)
# print(not 3 in nums)
# print(3 not in nums)

# items = [42, 88, 721, 12, 43, 22, 908]
# num = int(input())
# if num in items:
#     print('bingo')

# TODO: List Functions
#  max(list): возвращает элемент списка с максимальным значением
#  min(list): возвращает элемент списка с минимальным значением
#  list.count(item): возвращает счетчик того, сколько раз элемент встречается в списке
#  list.remove(item): удаляет объект из списка
#  list.reverse(): переворачивает элементы в списке
#  list.index('r'): возращает индекс элемента в списке, в случае отсутствия возращает ValueError
# nums = [1, 2, 3]
# nums.append(4)
# print(nums)

# words = ["hello"]
# words.append("world")
# print(words[1])

# nums = [1, 3, 5, 2, 4]
# print(len(nums))

# words = ["Python", "fun"]
# index = 1
# words.insert(index, "is")
# print(words)

# nums = [9, 8, 7, 6, 5]
# nums.append(4)
# nums.insert(2, 11)
# print(len(nums))
# print(nums)

# letters = ['p', 'q', 'r', 's', 'p', 'u']
# print(letters.index('r'))
# print(letters.index('p'))
# print(letters.index('z'))

# items = [2, 4, 6, 8, 10, 12, 14]
# print(len(items) // 2)

# TODO: while Loops используется в случаях, когда количество итераций неизвестно и
#  зависит от некоторых вычислений и условий в кодовом блоке цикла.
# i = 1
# while i <= 5:
#     print(i)
#     i += + 1
# print("Finished!")

# i = 3
# while i >= 0:
#     print(i)
#     i -= 1
# print("Finished!")

# i = 0
# while 1 == 1:
#     print(i)
#     i = i + 1
#     if i >= 5:
#         print("Breaking")
#         break
# print("Finished")

# i = 5
# while True:
#     print(i)
#     i = i - 1
#     if i <= 2:
#         break

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         print("Skipping 3")
#         continue
#     print(i)

# У вас есть волшебная коробка, которая удваивает количество предметов,
# которые вы кладете в нее каждый день. Данная программа принимает в
# качестве входных данных начальное количество предметов и количество дней.
# Задача Написать программу для подсчета и вывода количества товаров за последний день.
# items = int(input())
# days = int(input())
# while days > 0:
#     items *= 2
#     days -= 1
# print(items)

# TODO: for Loop: цикл for используется для перебора заданной последовательности, такой как списки или строки.
# words = ["hello", "world", "spam", "eggs"]
# for word in words:
#     print(word + "!")

# str = "testing for loops"
# count = 0
# for x in str:
#     if x == 'o':
#         count += 1
# print(count)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum = 0
# for i in list:
#     sum += i
# print(sum)

# TODO: Range: функция range() возвращает последовательность чисел.
#  По умолчанию он начинается с 0, увеличивается на 1 и останавливается перед указанным числом.
# numbers = list(range(10))
# print(numbers)

# nums = list(range(5))
# print(nums[4])

# numbers = list(range(3, 8))
# print(numbers)
# print(range(20) == range(0, 20))

# nums = list(range(5, 8))
# print(len(nums))

# numbers = list(range(5, 20, 2))
# print(numbers)

# nums = list(range(3, 15, 3))
# print(nums[2])

# for i in range(5):
#     print("hello!")

# a = int(input())
# b = int(input())
# print(list(range(a, b)))

# for i in range(10):
#     if not i % 2 == 0:
#         print(i + 1)

# letters = ['x', 'y', 'z']
# letters.insert(1, 'w')
# print(letters[2])

# n = int(input())
# for x in range(1, n):
#     if x % 3 == 0 and x % 5 == 0:
#         print("SoloLearn")
#     elif x % 3 == 0 and x % 2 != 0:
#         print("Solo")
#     elif x % 5 == 0 and x % 2 != 0:
#         print("Learn")
#     elif x % 2 == 0:
#         continue
#     else:
#         print(x)

# TODO: Reusing Code: Повторное использование кода — очень важная часть программирования на любом языке.
#  Увеличение размера кода усложняет его поддержку. Чтобы большой проект по программированию был успешным,
#  важно соблюдать принцип «Не повторяйся» или «СУХОЙ».

# TODO: Functions & Modules
# def my_func():
#     print("spam")
#     print("spam")
#     print("spam")
#
#
# my_func()

# def welcome_message():
#     name = input()
#     print(f"Welcome, {name}")
#
#
# welcome_message()

# TODO: Functions Arguments: Все определения функций, которые мы рассматривали до сих пор,
#  были функциями с нулевыми аргументами, которые вызываются с пустыми скобками.
#  Однако большинство функций принимают аргументы.
#  Параметры — это переменные в определении функции, а
#  Аргументы — это значения, помещаемые в параметры при вызове функций.
# def print_with_exclamation(word: str):
#     print(word + "!")
#
#
# print_with_exclamation("spam")
# print_with_exclamation("eggs")
# print_with_exclamation("python")

# def print_double(x):
#     print(2 * x)
#
#
# print_double(3)

# def function(variable):
#     variable += 1
#     print(variable)
#
#
# function(7)

# password = input()
# repeat = input()
#
#
# def validate(text1, text2):
#     if text1 == text2:
#         print('Correct')
#     else:
#         print('Wrong')
#
#
# validate(password, repeat)

# TODO: Returning from Functions: Некоторые функции, такие как int или str,
#  возвращают значение, которое можно использовать позже.
#  Чтобы сделать это для определенных вами функций, вы можете использовать оператор return
# def max(x, y):
#     if x >= y:
#         return x
#     else:
#         return y
#
#
# print(max(4, 7))
# z = max(8, 5)
# print(z)

# def add_numbers(x, y):
#     total = x + y
#     return total
#     print("This won't be printed")
#
#
# print(add_numbers(4, 5))

# def print_numbers():
#     print(1)
#     print(2)
#     return
#     print(4)
#     print(6)
#
#
# print_numbers()

# s = input()
#
#
# def hashtagGen(text):
#     return "#" + text.replace(" ", "")
#
#
# print(hashtagGen(s))

# def multiply(x, y):
#     return x * y
#
#
# a = 4
# b = 7
# operation = multiply
# print(operation(a, b))

# def add(x, y):
#     return x + y
#
#
# def minus(x, y):
#     return x - y
#
#
# def mult(x, y):
#     return x * y
#
#
# def do_twice(func, x, y):
#     return func(func(x, y), func(x, y))
#
#
# a = 5
# b = 10
#
# print(do_twice(add, a, b))
# print(do_twice(mult, a, b))
# print(do_twice(minus, a, b))

# def square(x):
#     return x * x
#
#
# def inc(x):
#     return x + 1
#
#
# def test(func, x):
#     print(func(x))
#
#
# test(square, 5)
# test(inc, 5)

# TODO: Comments: комментарии — это аннотации к коду, используемые для облегчения его понимания.
#  Они не влияют на выполнение кода. В Python комментарий создается путем вставки октоторпа
#  (также известного как знак числа или символ решетки: #). Весь текст после него в этой строке игнорируется.

# x = 365
# y = 7
# # this is a comment
#
# print(x % y)  # find the remainder
# # print (x // y)
# # another comment

# TODO: Docstrings: строки документации служат той же цели, что и комментарии,
#  поскольку они предназначены для пояснения кода. Однако они более специфичны и
#  имеют другой синтаксис. Они создаются путем размещения многострочной строки,
#  содержащей объяснение функции, под первой строкой функции.
# def shout(word):
#     """
#     Print a word with an
#     exclamation mark following it.
#     """
#     print(word + "!")
#
#
# shout("spam")

# TODO: Modules. Модули — это фрагменты кода, которые другие люди написали для выполнения общих задач,
#  таких как генерация случайных чисел, выполнение математических операций и т.д.
# import random
#
# for i in range(5):
#     value = random.randint(1, 6)
#     print(value)

# import random
# random.seed(int(input()))
#
# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)
#
# print(dice1)
# print(dice2)


# import math
#
# num = 10
# print(math.sqrt(num))
# print(math.factorial(num))

# from math import pi, sqrt
#
# print(pi)
# print(sqrt(9))

# from math import sqrt as square_root
# print(square_root(100))

# import math as m
#
# print(m.sqrt(25))

# def print_nums(x):
#     for i in range(x):
#         print(i)
#         return
#
#
# print_nums(10)


# def func(x):
#     res = 0
#     for i in range(x):
#         res += i
#         print(i)
#     return res
#
#
# print(func(4))

# celsius = int(input())
#
#
# def conv(c):
#     return 9/5 * c + 32
#
#
# fahrenheit = conv(celsius)
# print(fahrenheit)

#  TODO: Exceptions: исключения возникают, когда что-то идет не так,
#   из-за неправильного кода или ввода. При возникновении исключения программа немедленно останавливается.
#   ImportError : сбой импорта;
#   IndexError : список проиндексирован с номером вне допустимого диапазона;
#   NameError : используется неизвестная переменная;
#   SyntaxError : код не может быть проанализирован должным образом;
#   TypeError : функция вызывается для значения неподходящего типа;
#   ValueError : функция вызывается для значения правильного типа, но с неподходящим значением;
#   ZeroDivisionError: деление на ноль;
#   OSError: используемое для описания системных ошибок.
# num1 = 7
# num2 = 0
# print(num1/num2)

# print("7" + 4)

# try:
#     pin = int(input())
#     print("PIN code is created")
# except ValueError:
#     print("Please enter a number")

# try:
#     num1 = 7
#     num2 = 0
#     print(num1 / num2)
#     print("Done calculation")
# except ZeroDivisionError:
#     print("An error occurred")
#     print("due to zero division")

# try:
#     variable = 10
#     print(10 / 2)
# except ZeroDivisionError:
#     print("Error")
# print("Finished")

# try:
#     variable = 10
#     print(variable + "hello")
#     print(variable / 2)
# except ZeroDivisionError:
#     print("Divided by zero")
# except (ValueError, TypeError):
#     print("Error occurred")

# try:
#     meaning = 42
#     print(meaning / 0)
#     print("the meaning of life")
# except (ValueError, TypeError):
#     print("ValueError or TypeError occurred")
# except ZeroDivisionError:
#     print("Divided by zero")

# try:
#     word = "spam"
#     print(word / 0)
# except:
#     print("An error occurred")

#  TODO: finally - используется чтобы убедиться, что какой-то код работает независимо от того, какие ошибки возникают.
#   Помещается в конец оператора try/except, запускается после выполнения кода в блоках try/except.
# try:
#     print("Hello")
#     print(1 / 0)
# except ZeroDivisionError:
#     print("Divided by zero")
# finally:
#     print("This code will run no matter what")

# try:
#     print(1)
# except:
#     print(2)
# finally:
#     print(3)

# try:
#     print(1)
#     print(10 / 0)
# except ZeroDivisionError:
#     print(unknown_var)
# finally:
#     print("This is executed last")

# coffee = ["Caff Latte", "Caffe Americano", "Espresso", "Cappuccino", "Machination"]
# choice = int(input())
# try:
#     print(coffee[choice])
# except:
#     print('Invalid number')
#
# finally:
#     print('Have a good day')

#  TODO: raise
# print(1)
# raise ValueError
# print(2)

# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     raise ValueError

# name = "123"
# raise NameError("Invalid name!")

# try:
#     num = 5 / 0
# except:
#     print("An error occurred")
#     raise

#  TODO: Assertions - это проверка работоспособности,
#   которую можно включить или выключить после завершения тестирования программы.
#   Выражение проверяется, и если результат оказывается ложным, возникает исключение.
#   Утверждения выполняются с помощью оператора assert .
# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)

# print(0)
# assert "h" != "w"
# print(1)
# assert False
# print(2)
# assert True
# print(3)

# temp = -10
# assert (temp >= 0), "Colder than absolute zero!"

# TODO: Opening Files - Вы можете использовать Python для чтения и записи содержимого файлов. Текстовыми файлами легче
#  всего манипулировать. Прежде чем файл можно будет отредактировать, его необходимо открыть с помощью функции
#  open.
# myfile = open("C:/Users/User/PycharmProjects/SQLite/filename.txt")

# # write mode
# open("filename.txt", "w")
#
# # read mode
# open("filename.txt", "r")
# open("filename.txt")
#
# # binary write mode
# open("filename.txt", "wb")

# file = open("filename.txt", "w")
# # do stuff to the file
# file.close()

# TODO: Reading Files
# file = open("filename.txt", "r")
# cont = file.read()
# print(cont)
# file.close()

# file = open("filename.txt", "r")
# print(file.read(16))
# print(file.read(4))
# print(file.read(4))
# print(file.read())
# file.close()

# file = open("filename.txt", "r")
# cont = file.read()
# print(cont)
# file.close()

# file = open("filename.txt", "r")
# for i in range(21):
#     print(file.read(4))
# file.close()

# file = open("filename.txt", "r")
# file.read()
# print("Re-reading")
# print(file.read())
# print("Finished")
# file.close()

# прочитать количество строк файла
# file = open("filename.txt", "r")
# str = file.read()
# print(len(str))
# file.close()

# Чтобы получить каждую строку в файле, вы можете использовать метод readiness() для возврата списка,
# в котором каждый элемент является строкой
# file = open("filename.txt", "r")
# print(file.readlines())
# file.close()

# Можно использовать цикл for для перебора строк в файле:
# file = open("filename.txt", "r")
#
# for line in file:
#     print(line)
#
# file.close()

# number_of_lines = len(open("filename.txt").readlines())
# print(number_of_lines)

# file = open("/usercode/files/pull_ups.txt")
# n = int(input())
#
# print(file.readlines()[n])
#
# file.close()

# file = open("filename2.txt", "w")
# file.write("This has been written to a file")
# file.close()
#
# file = open("filename2.txt", "r")
# print(file.read())
# file.close()

# file = open("filename2.txt", "w")
# file.write("Some new text")
# file.close()
#
# file = open("filename2.txt", "r")
# print("Reading new contents")
# print(file.read())
# print("Finished")
# file.close()

# msg = "Hello world!"
# file = open("filename2.txt", "w")
# amount_written = file.write(msg)
# print(amount_written)
# file.close()

# file = open("filename2.txt", "w")
# file.write("Some new text")
# print(file.write("Some new text"))
# file.close()
#
# file = open("filename2.txt", "r")
# print("Reading new contents")
# print(file.read())
# print("Finished")
# file.close()

# names = ["John", "Oscar", "Jacob"]
#
# file = open("filename2.txt", "w+")
# for i in names:
#     file.write(i + "\n")
# file.close()
#
# file = open("filename2.txt", "r")
# print(file.read())
# file.close()

# try:
#     f = open("filename.txt")
#     print(f.read())
# finally:
#     f.close()

# try:
#     f = open("filename.txt")
#     print(f.read())
#     print(1 / 0)
# finally:
#     f.close()

# # Файл автоматически закрывается в конце оператора with , даже если в нем возникают исключения.
# with open("filename.txt") as f:
#     print(f.read())

# try:
#     print(1)
#     assert 2 + 2 == 5
# except AssertionError:
#     print(3)
# except:
#     print(4)

# file = open("filename2.txt", "r")
# for line in file.readlines():
#     print(f'{line[0]}{len(line.strip())}')
# file.close()

# код выше можно записать в две строки:
# for line in open("filename2.txt", "r"):
#     print(f'{line[0]}{len(line.strip())}')

#  TODO: None - объект None используется для представления отсутствия значения
# print(None)

# def some_func():
#     print("Hi!")
#
#
# var = some_func()
# print(var)

# foo = print()
# if foo == None:
#     print(1)
# else:
#     print(2)

#  TODO: Dictionaries - это структуры данных, используемые для сопоставления произвольных ключей со значениями
# ages = {"Dave": 24, "Mary": 42, "John": 58, 'BMW': "black", 'VOLVO': 'white', 'cs-stroy@mail.ru': 'dkd2020202$$CSS'}
# print(ages["Dave"])
# print(ages["Mary"])
# print(ages["BMW"])
# print(ages['cs-stroy@mail.ru'])

# primary = {
#     "red": [255, 0, 0],
#     "green": [0, 255, 0],
#     "blue": [0, 0, 255],
# }
# # Попытка проиндексировать ключ, который не является частью словаря, возвращает KeyError
# print(primary["red"])
# print(primary["yellow"])

# # Попытка проиндексировать ключ, который не является частью словаря, возвращает KeyError
# test = {}
# print(test[0])

# # В качестве ключей к словарям можно использовать только неизменяемые объекты.
# # Неизменяемые объекты — это объекты, которые нельзя изменить
# bad_dict = {
#     [1, 2, 3]: "one two three",
# }

# store = {"Orange": 2, "Watermelon": 0, "Apple": 8, "Banana": 42}
# print(store["Apple"])

# squares = {0: 1, 1: 2, 2: "error", 3: 4}
# squares[4] = 5
# squares[2] = 3
# print(squares)

# primes = {1: 2, 2: 3, 4: 7, 7: 17}
# # print(primes[4])
# # print(primes[7])
# print(primes[primes[4]])

# # Чтобы определить, находится ли ключ в словаре, можно использовать in и not in так же, как и для списка.
# nums = {
#     1: "one",
#     2: "two",
#     3: "three",
# }
# print(1 in nums)
# print("three" in nums)
# print(4 not in nums)

# # Полезным словарным методом является get .
# # Он делает то же самое, что и индексация, но если ключ не найден в словаре,
# # вместо этого возвращается другое указанное через запятую значение (по умолчанию «None»).
# pairs = {1: "apple",
#          "orange": [2, 3, 4],
#          True: False,
#          None: "True",
#          }
#
# print(pairs.get("orange"))
# print(pairs.get(7))
# print(pairs.get(12345, "not in dictionary"))

# fib = {1: 1, 2: 1, 3: 2, 4: 3}
# print(fib.get(4, 0) + fib.get(7, 5))

# books = {
#     "Life of Pi": "Adventure Fiction",
#     "The Three Musketeers": "Historical Adventure",
#     "Watchmen": "Comics",
#     "Bird Box": "Horror",
#     "Harry Potter": "Fantasy Fiction",
#     "Good Omens": "Comedy"
# }
#
# book = input()
# print(books.get(book, "Book not found"))

#  TODO: Tuples - кортежи очень похожи на списки, за исключением того, что они неизменяемы (их нельзя изменить).
#   Кортежи быстрее, чем списки, но их нельзя изменить.
# words = ("spam", "eggs", "sausages",)
# print(words[0])  # можем получить доступ к значениям в кортеже с их индексом, как и со списками.
# words[1] = "cheese"  # Попытка переназначить значение в кортеже приводит к ошибке TypeError.

# # Кортежи можно создавать без круглых скобок, просто разделяя значения запятыми:
# my_tuple = "one", "two", "three"
# print(my_tuple[0])

# # Пустой кортеж создается с помощью пустой пары скобок.
# tpl = ()

# import math
#
# p1 = (23, -88)
# p2 = (6, 42)
# print(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))
