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

# TODO: String Formatting — Форматирование строк предоставляет более мощный способ встраивания не строк в строки.
#  Форматирование строки использует метод форматирования строки для замены ряда аргументов в строке.
# nums = [4, 5, 6]
# msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
# nms = f"Numbers: {nums[0]} {nums[1]} {nums[2]}"
# print(msg)
# print(nms)

# print("{0}{1}{0}".format("abra", "cad"))

# a = "{x}, {y}".format(x=5, y=12)
# print(a)

#  TODO: String Functions
#   join - объединяет список строк с другой строкой в качестве разделителя. Из списка в строку.
#   replace - заменяет одну подстроку в строке на другую.
#   startswith and endswith - определяют, есть ли подстрока в начале и в конце строки соответственно.
#   lower and upper - чтобы изменить регистр строки на нижний и верхний.
#   split - противоположен join, превращающему строку с определенным разделителем в список. Из строки в список.

# print(", ".join(["spam", "eggs", "ham"]))
# # prints "spam, eggs, ham"
#
# print("Hello ME".replace("ME", "world"))
# # prints "Hello world"
#
# print("This is a sentence.".startswith("This"))
# # prints "True"
#
# print("This is a sentence.".endswith("sentence."))
# # prints "True"
#
# print("This is a sentence.".upper())
# # prints "THIS IS A SENTENCE."
#
# print("AN ALL CAPS SENTENCE".lower())
# # prints "an all caps sentence"
#
# string = "This is a sentence."
# print(f'{string[0:4].upper()} {string[4::].lower()}')
# # prints "THIS  is a sentence."
#
# print("spam, eggs, ham".split(", "))
# # prints "['spam', 'eggs', 'ham']"

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

#  TODO: Numeric Functions -
#   max or min  - чтобы найти максимум или минимум некоторых чисел или списка.
#   abs - чтобы найти расстояние числа от нуля (его абсолютное значение).
#   round - чтобы округлить число до определенного количества знаков после запятой.
#   sum - чтобы найти итог списка.
# print(min(1, 2, 3, -4, 0, 2, 1))
# print(max([1, 4, 9, 2, 5, 6, 8]))
# print(abs(-99))
# print(abs(42))
# print(round(77.394953738, 3))
# print(sum([1, 2, 3, 4, 5]))

# a = min([sum([11, 22]), max(abs(-30), 2)])
# print(a)

#  TODO: List Functions -
#   all и any принимают список в качестве аргумента и возвращают True,
#   если все или некоторые (соответственно) их аргументы оцениваются как True (и False в противном случае).
#   enumerate может использоваться для одновременного перебора значений и индексов списка.
# nums = [55, 44, 33, 22, 11]
#
# if all([i > 5 for i in nums]):
#     print("All larger than 5")
# else:
#     print('not all over 5')
#
# if any([i % 2 == 0 for i in nums]):
#     print("At least one is even")
# else:
#     print('Not one is even')
#
# for v in enumerate(nums):
#     print(v)

# nums = [-1, 2, -3, 4, -5]
# if all([abs(i) < 3 for i in nums]):
#     print(1)
# else:
#     print(2)

# txt = input()
# print(txt.replace('#', ' '))

# TODO: Text Analyzer - анализирует образец файла, чтобы определить, какой процент текста занимает каждый символ
# filename = input("Enter a filename: ")
#
# with open(filename) as f:
#     text = f.read()
#
# print(text)

# def count_char(text, char):  # функция, которая подсчитывает, сколько раз символ встречается в строке.
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count
#
#
# filename = input("Enter a filename: ")  # функция принимает в качестве аргументов текст файла и один символ,
# with open(filename) as f:  # возвращая количество раз, которое этот символ появляется в тексте.
#     text = f.read()
#
# print(count_char(text, "1"))
#
# for char in "abcdefghijklmnopqrstuvwxyz":
#     perc = 100 * count_char(text, char) / len(text)
#     print("{0} - {1}%".format(char, round(perc, 2)))

# # программа находит, какой процент текста занимает каждый символ английского алфавита,
# # в только что созданном программой файле newfile.txt.
# def count_char(text, char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count
#
#
# file = open("newfile.txt", "w")
# file.write("""Ornhgvshy vf orggre guna htyl.
# Rkcyvpvg vf orggre guna vzcyvpvg.
# Fvzcyr vf orggre guna pbzcyvpngrq.
# Syng vf orggre guna arfgrq.
# Fcenfr fv orggre guna qrafr.
# Ernqnovyvgl pbhagf.
# Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
# Nygubhtu cenpgvpnyvgl orgnf chevgl.
# Reebef fubhyq arire cnff fvyragyl.
# Hayrff rkcyvpvgyl fvyraprq.
# Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
# Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
# Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
# Abj vf orggre guna arrire.
# Nygubhtu arire vf bsgra orggre guna *evtug* abj.
# Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
# Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
# Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")
# file.close()
# filename = "newfile.txt"
# with open(filename) as f:
#     text = f.read()
#
# for char in "abcdefghijklmnopqrstuvwxyz":
#     perc = 100 * count_char(text, char) / len(text)
#     print(f'{char} - {round(perc, 2)}%')
# print(f'Текст состоит из {len(text)} символов')


# # программа находит, какой процент текста занимает каждый символ белорусского алфавита в файле newfileBY.txt
# def count_char(text, char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count
#
#
# filename = "newfileBY.txt"
# with open(filename) as f:
#     text = f.read()
#
# for char in "абвгдеёжзійклмнопрстуўфхцчшыьэюя":
#     perc = 100 * count_char(text, char) / len(text)
#     print(f'{char} - {round(perc, 2)}%')
# print(f'Текст состоит из {len(text)} символов')

# Задача: Дан текст на входе, выведите количество содержащихся в нем слов.
# Пример ввода: hello world
# Пример вывода: 2
# txt = input()
# a = txt.split()
# print(len(a))

# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]), abs(-42)))

# txt = input()
# list_words = txt.split()
# print(max(list_words, key=len))

# # код выше, но записанный в 2 строки:
# txt = input().split()
# print(max(txt, key=len))

#  TODO: Functional Programming - это стиль программирования, который (как следует из названия) основан на функциях.
# def apply_twice(func, arg):  # Функция apply_twice принимает в качестве аргумента другую функцию
#     return func(func(arg))  # и дважды вызывает ее внутри своего тела.
#
#
# def add_five(x):
#     return x + 5
#
#
# print(apply_twice(add_five, 10))


# def test(func, arg):
#     return func(func(arg))
#
#
# def mult(x):
#     return x * x
#
#
# print(test(mult, 2))

#  TODO: Pure Functions - Чистые функции не имеют побочных эффектов и возвращают значение,
#   которое зависит только от их аргументов.
# def pure_function(x, y):  # Чистая функция
#     temp = x + 2 * y
#     return temp / (2 * x + y)
#
#
# print(pure_function(2, 4))

# def func(x):  # Чистая функция
#     y = x ** 2
#     z = x + y
#     return z

# some_list = []
#
#
# def impure(arg):  # Не чистая функция, потому что она изменила состояние some_list
#     some_list.append(arg)
#
#
# impure('Не')
# impure('чистая')
# impure('функция')
# impure(', потому что она изменила состояние some_list')
# print(some_list)

#  TODO: Lambdas - Лямбда-функции получили свое название от лямбда-исчисления — модели вычислений,
#   изобретенной Алонзо Чёрчем. Лямбда-функции можно создавать на лету, не присваивая их переменной.
# def my_func(f, arg):
#     return f(arg)
#
#
# print(my_func(lambda x: 2 * x * x, 5))

# # named function
# def polynomial(x):
#     return x ** 2 + 5 * x + 4
#
#
# print(polynomial(-4))

# # lambda
# print((lambda x: x ** 2 + 5 * x + 4)(-4))

# a = (lambda x: x * x)(8)
# print(a)

# double = lambda x: x * 2
# print(double(7))

# triple = lambda x: x * 3
# add = lambda x, y: x + y
# print(add(triple(3), 4))

# x = int(input())
# y = (lambda z:z*z*z)(x)
# print(y)

#  TODO: map - Встроенные функции map и filter — это очень полезные функции высшего порядка,
#   которые работают со списками (или подобными объектами, называемыми итерируемыми).
#   map - принимает функцию и итерируемый объект в качестве аргументов и возвращает
#   новый итерируемый объект с функцией, примененной к каждому аргументу.
# def add_five(x):
#     return x + 5
#
#
# nums = [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)

# # можем бы добиться того же результата более легко, используя лямбда - синтаксис:
# nums = [11, 22, 33, 44, 55]
# result = list(map(lambda x: x + 5, nums))
# print(result)

#  TODO: filter - фильтрует итерируемый объект, удаляя элементы,
#   не соответствующие предикату (функция, возвращающая логическое значение).
#   Как и map, результат должен быть явно преобразован в список, если вы хотите его распечатать.
# nums = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)

# nums = [1, 2, 5, 8, 3, 0, 7]
# res = list(filter(lambda x: x < 5, nums))
# print(res)

# names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]
# res = list(filter(lambda x: len(x) > 5, names))
# print(res)

# #       01234567890123456789012345678901
# text = 'абвгдеёжзійклмнопрстуўфхцчшыьэюя'
# a = f'{text[13]}{text[5]}{text[14]}{text[18]}{text[11]}'
# print(a.upper())

# TODO: Generators - тип итерируемых объектов, таких как списки или кортежи.
#  В отличие от списков, они не допускают индексации с произвольными индексами,
#  но их все же можно перебирать с помощью циклов for.
#  Их можно создать с помощью функций и оператора yield
# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i -= 1
#
#
# # Короче говоря, генераторы позволяют вам объявить функцию, которая ведет себя как итератор,
# # и ее можно использовать в цикле for.
# for x in countdown():
#     print(x)

# def infinite_sevens():
#     while True:
#         yield 7
#
#
# for i in infinite_sevens():
#     print(i)

# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#
#     return True
#
#
# def get_primes():
#     num = 2
#     while True:
#         if is_prime(num):
#             yield num
#         num += 1
#
#
# for x in get_primes():
#     print(x)

# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i
#
#
# print(list(numbers(11)))


# def make_word():
#     word = ""
#     for ch in "spam":
#         word += ch
#         yield word
#
#
# print(list(make_word()))

# txt = input()
#
#
# def words(t):
#     yield t.split()
#
#
# for x in words(txt):
#     print(x)

#  TODO: Decorators - позволяют изменять функции, используя другие функции.
#   Это идеально, когда Вам нужно расширить функциональность функций, которые вы не хотите изменять.
# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#
#     return wrap
#
#
# def print_text():
#     print("Hello world!")
#
#
# decorated = decor(print_text)
# decorated()


# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#
#     return wrap
#
#
# def print_text():
#     print("Hello world!")
#
#
# print_text = decor(print_text)
# print_text()

# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#
#     return wrap
#
#
# @decor
# def print_text():
#     print("Hello world!")
#
#
# print_text()

# text = input()
#
#
# def uppercase_decorator(func):
#     def wrapper(t):
#         return t.upper()
#
#     return wrapper
#
#
# @uppercase_decorator
# def display_text(x):
#     return x
#
#
# print(display_text(text))

# def uppercase_decorator(func):
#     def wrapper(t):
#         return t.upper()
#
#     return wrapper
#
#
# @uppercase_decorator
# def display_text(x):
#     return x
#
#
# print(display_text('text'))

# def decorator_a(fun):
#     print('Get in decorator_a')
#
#     def inner_a(*args, **kwargs):
#         print('Get in inner_a')
#         res = fun(*args, **kwargs)
#         return res
#
#     return inner_a
#
#
# def decorator_b(fun):
#     print('Get in decorator_b')
#
#     def inner_b(*args, **kwargs):
#         print('Get in inner_b')
#         res = fun(*args, **kwargs)
#         return res
#
#     return inner_b
#
#
# @decorator_a
# @decorator_b
# def f(x):
#     print('Get in f')
#     return x * 2
#
#
# f(2)

# TODO: Recursion -  очень важная концепция в функциональном программировании.
#   Фундаментальной частью рекурсии является самоссылка — функции, вызывающей саму себя.
#   Используется для решения проблем, которые можно разбить на более простые подзадачи того же типа.
#   Классическим примером рекурсивно реализованной функции является функция факториала.
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
# print(factorial(5))

# def is_even(x):
#     if x == 0:
#         return True
#     else:
#         return is_odd(x - 1)
#
#
# def is_odd(x):
#     return not is_even(x)
#
#
# print(is_odd(1))
# print(is_even(3))


# def fib(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
#
#
# print(fib(4))

# def calc(list):
#     if len(list) == 0:
#         return 0
#     else:
#         return list[0]**2 + calc(list[1:])
#
#
# list = [1, 3, 4, 2, 5]
# x = calc(list)
# print(x)

# TODO: Sets - это структуры данных, похожие на списки или словари.
#  Они создаются с помощью фигурных скобок {} или функции set().
#  Они имеют некоторые общие функции со списками, такие как использование in для проверки того,
#  содержат ли они определенный элемент.
#  Наборы отличаются от списков несколькими способами, но имеют несколько общих операций со списками, таких как len().
#  Они неупорядочены, что означает, что они не могут быть проиндексированы.
#  Они не могут содержать повторяющиеся элементы!!!
#  Из-за того, как они хранятся, быстрее проверить, является ли элемент частью набора, а не частью списка.
#  Вместо использования append для добавления в набор используйте add().
#  Метод remove() удаляет определенный элемент из набора; pop() удаляет произвольный элемент.

# num_set = {1, 2, 3, 4, 5}
# word_set = set(["spam", "eggs", "sausage"])
#
# print(3 in num_set)
# print("spam" not in word_set)

# letters = {"a", "b", "c", "d"}
# if "e" not in letters:
#     print(1)
# else:
#     print(2)

# nums = {1, 2, 1, 3, 1, 4, 5, 6}
# print(nums)
# nums.add(-7)
# nums.remove(3)
# print(nums)

# nums = {"a", "b", "c", "d"}
# nums.add("z")
# print(len(nums))
# TODO: Sets наборы можно комбинировать с помощью математических операций:
#  Оператор объединения | объединяет два набора, чтобы сформировать новый, содержащий элементы в любом из них.
#  Оператор пересечения & получает элементы только в обоих случаях.
#  Оператор разности    - получает элементы в первом наборе, но не во втором.
#  Оператор симметричной разности ^ получает элементы в любом наборе, но не в обоих одновременно.
# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}
#
# print(first | second)
# print(first & second)
# print(first - second)
# print(second - first)
# print(first ^ second)

# a = {1, 2, 3}
# b = {0, 3, 4, 5}
# print(a & b)

# TODO: Data Structures (Структуры данных) - списки, словари, кортежи, наборы.
#  Когда использовать словарь: - если нужна логическая ассоциация между парой ключ: значение и нужен быстрый поиск
#  данных на основе пользовательского ключа, если данные постоянно изменяются, словари изменяемы.
#  Когда использовать списки: - если есть коллекция данных, не требующая произвольного доступа и
#  нужна простая итерируемая коллекция, которая часто изменяется.
#  Когда использовать Set (набор): - если нужна уникальность для элементов.
#  Когда использовать кортежи: - если данные не могут измениться.
# set1 = {2, 4, 5, 6}
# set2 = {4, 6, 7, 8, 11, 42, 2}
# print(set1 & set2)

# a = (2, 3, 2, 3)
# print(a)
# b = {2, 3, 2, 3}
# print(b)
# print(len(b))

# TODO: itertools - Модуль itertools — это стандартная библиотека, содержащая несколько функций,
#  полезных в функциональном программировании.
#  Один из типов функций, которые он производит — это бесконечные итераторы.
#  Функция count бесконечно увеличивает значение.
#  Функциональный cycle бесконечно перебирает итерируемый объект (например, список или строку).
#  Функция repeat повторяет объект либо бесконечно, либо определенное количество раз.
#  Функция takewhile - берет элементы из итерации, пока функция предиката остается истинной.
#  Функция chain - объединяет несколько итераций в одну длинную.
#  Функция accumulate - возвращает промежуточную сумму значений в итерации.
#  Функции product (произведение) and permutation (перестановка) - комбинаторные функции,
#  используются для выполнения задач со всеми возможными комбинациями некоторых элементов.

# from itertools import count
#
# for i in count(3):
#     print(i)
#     if i >= 11:
#         break

# from itertools import accumulate, takewhile
#
# nums = list(accumulate(range(8)))
# print(nums)
# print(list(takewhile(lambda x: x <= 15, nums)))

# from itertools import takewhile
#
# nums = [2, 4, 6, 8, 7, 9, 8]
# a = takewhile(lambda x: x % 2 == 0, nums)
# print(list(a))

# from itertools import product, permutations
#
# letters = ("A", "B")
# print(list(product(letters, range(2))))
# print(list(permutations(letters)))

# from itertools import product
#
# a = {1, 2}
# print(list(product(range(3), a)))
# print(len(list(product(range(3), a))))

# from itertools import permutations
#
# items = ['x', 'y']
# print(list(permutations(items)))

# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# print(nums)
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))

# def power(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x, y - 1)
#
#
# print(power(3, 4))

# a = (lambda x: x * (x + 1))(6)
# print(a)

# nums = [1, 2, 8, 3, 7]
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)

# num = int(input())
#
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(num):
#     print(fibonacci(i))

# TODO: Classes - Ранее мы рассмотрели две парадигмы программирования — императивную (использующую операторы,
#  циклы и функции в качестве подпрограмм) и функциональную (использующую чистые функции,
#  функции высшего порядка и рекурсию). Другой очень популярной парадигмой является
#  объектно-ориентированное программирование (ООП). Объекты создаются с использованием классов,
#  которые на самом деле являются фокусом ООП. Класс описывает, каким будет объект, но он отделен от самого объекта.
#  Другими словами, класс можно описать как схему, описание или определение объекта.
#  Вы можете использовать один и тот же класс в качестве схемы для создания нескольких разных объектов.
# class Cat:
#     """
#     Классы создаются с использованием ключевого слова class и блока с отступом,
#     который содержит методы класса (которые являются функциями).
#     Этот код определяет класс с именем Cat, который имеет два атрибута: цвет и ноги .
#     """
#
#     def __init__(self, color, legs):
#         self.color = color
#         self.legs = legs
#
#
# """
# Класс Cat используется для создания 3 отдельных объектов этого класса.
# """
# felix = Cat("ginger", 4)
# rover = Cat("dog-colored", 4)
# stumpy = Cat("brown", 3)


# TODO: __init__ - самый важный метод в классе.
#  Это вызывается при создании экземпляра (объекта) класса с использованием имени класса в качестве функции.
#  Все методы должны иметь self в качестве первого параметра, хотя он не передается явно,
#  Python добавляет аргумент self в список за вас; вам не нужно включать его при вызове методов.
#  В определении метода self ссылается на экземпляр, вызывающий метод. Экземпляры класса имеют атрибуты,
#  которые представляют собой фрагменты данных, связанные с ними.
#  В этом примере экземпляры Cat имеют атрибуты цвета и ног.
#  Доступ к ним можно получить, поставив точку и имя атрибута после экземпляра.
# class Cat:
#     """
#     в методе __init__ self.attribute можно использовать для установки начального значения атрибутов экземпляра.
#     Метод __init__ принимает два аргумента и присваивает их атрибутам объекта.
#     Метод __init__ называется конструктором класса.
#     """
#     def __init__(self, color, legs):
#         self.color = color
#         self.legs = legs
#
#
# felix = Cat("ginger", 4)
# print(felix.color)

# TODO: Methods - Классы могут иметь другие методы, определенные для добавления функциональности.
#  Все методы должны иметь self в качестве первого параметра.
#  Доступ к этим методам осуществляется с использованием того же синтаксиса точек, что и у атрибутов.
# class Dog:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def bark(self):
#         print("Woof!")
#
#
# fido = Dog("Fido", "brown")
# print(fido.name)
# fido.bark()


# class Dog:
#     """
#     Классы также могут иметь атрибуты класса, созданные путем присвоения переменных в теле класса.
#     Доступ к ним можно получить либо из экземпляров класса, либо из самого класса.
#     Атрибуты класса являются общими для всех экземпляров класса.
#     """
#     legs = 4
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
# fido = Dog("Fido", "brown")
# print(fido.legs)
# print(Dog.legs)

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def sayHi(self):
#         print("Hi from " + self.name)
#
#
# s1 = Student("Amy")
# s1.sayHi()

# class Rectangle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = f'Цвет треугольника: {color}'
#
#     def get_area(self):
#         print(f'Площадь прямоугольника: {self.width * self.height}м2')
#
#     def get_perimeter(self):
#         print(f'Периметр прямоугольника: {2 * (self.width + self.height)}м2')
#
#
# rect = Rectangle(7, 8, 'black')
# print(rect.color)
# rect.get_area()
# rect.get_perimeter()

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(self.name + " says hi")
#
#
# obj = Student("John")
# obj.greet()

# TODO: Inheritance - Наследование позволяет разделить функциональность между классами.
#  Представьте себе несколько классов: Cat, Dog, Rabbit и так далее.
#  Хотя они могут в чем-то отличаться (только у Dog может быть метод bark), у других они,
#  скорее всего, будут похожи (все имеют атрибуты color и name) - это сходство можно выразить,
#  заставив их всех наследовать от суперкласса Animal, который содержит общие функции.
#  Чтобы наследовать класс от другого класса, поместите имя суперкласса в круглых скобках после имени класса.
# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
# class Cat(Animal):
#     def purr(self):
#         print("Purr...")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")
#
#
# fido = Dog("Fido", "brown")
# print(fido.color)
# fido.bark()

# """
# Класс, который наследуется от другого класса, называется подклассом.
# Класс, который наследуют, называется суперклассом.
# Если класс наследуется от другого с теми же атрибутами или методами, он переопределяет их.
# В примере Wolf — это надкласс, а Dog — подкласс.
# """
#
#
# class Wolf:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def bark(self):
#         print("Grr...")
#
#
# class Dog(Wolf):
#     def bark(self):
#         print("Woof")
#
#
# husky = Dog("Max", "grey")
# husky.bark()

# class A:
#     def method(self):
#         print(1)
#
#
# class B(A):
#     def method(self):
#         print(2)
#
#
# B().method()

# """
# Наследование может быть и косвенным.
# Один класс может наследовать от другого, а тот класс может наследовать от третьего класса.
# Однако циклическое наследование невозможно.
# """
#
#
# class A:
#     def method(self):
#         print("A method")
#
#
# class B(A):
#     def another_method(self):
#         print("B method")
#
#
# class C(B):
#     def third_method(self):
#         print("C method")
#
#
# c = C()
# c.method()
# c.another_method()
# c.third_method()

# class A:
#     def a(self):
#         print(1)
#
#
# class B(A):
#     def a(self):
#         print(2)
#
#
# class C(B):
#     def c(self):
#         print(3)
#
#
# c = C()
# c.a()

# """
# Функция super — полезная функция, связанная с наследованием, которая ссылается на родительский класс.
# Его можно использовать для поиска метода с определенным именем в суперклассе объекта.
# super().spam() вызывает spam - метод суперкласса.
# """
#
#
# class A:
#     def spam(self):
#         print(1)
#
#
# class B(A):
#     def spam(self):
#         print(2)
#         super().spam()
#
#
# B().spam()


# """
# Завершите предоставленный код, чтобы наследовать класс Car от класса Vehicle,
# создайте объект Car и вызовите его метод horn(), унаследованный от суперкласса Vehicle.
# """
#
#
# class Vehicle:
#     def horn(self):
#         print("Beep!")
#
#
# class Car(Vehicle):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
# obj = Car("BMW", "red")
# obj.horn()

# TODO: Magic Methods (Магические методы) — это специальные методы, имена которых имеют двойное подчеркивание в
#  начале и в конце. Они также известны как дандеры. Пока что мы столкнулись только с __init__ ,
#  но есть и несколько других. Они используются для создания функциональности,
#  которую нельзя представить в виде обычного метода.
#  Одним из их распространенных применений является перегрузка операторов.
#  Это означает определение операторов для пользовательских классов,
#  которые позволяют использовать в них такие операторы, как + и *.
# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)
#
#
# """
# Метод __add__ позволяет определить пользовательское поведение для оператора + в нашем классе.
# Как видите, он добавляет соответствующие атрибуты объектов и возвращает новый объект, содержащий результат.
# Как только он определен, мы можем добавить два объекта класса вместе.
# """
# first = Vector2D(5, 7)
# second = Vector2D(3, 9)
# result = first + second
# print(result.x)
# print(result.y)

# """
# Метод __add__ позволяет определить пользовательское поведение для оператора + в нашем классе.
# Предоставленный код пытается сложить вместе два объекта BankAccount, в результате чего должен
# получиться новый объект с суммой остатков на указанных счетах. Исправьте код,
# чтобы он работал должным образом, и выведите итоговый баланс счета.
#
# Метод __add__ должен принимать 2 параметра, которые представляют добавляемые вами объекты
# """
#
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def __add__(self, other):
#         return BankAccount(self.balance + other.balance)
#
#
# a = BankAccount(1024)
# b = BankAccount(42)
#
# result = a + b
# print(result.balance)

# TODO: Магические методы для общих операторов:
#  __add__ для +
#  __sub__ for -
#  __mul__ for *
#  __truediv__ for /
#  __floordiv__ for //
#  __mod__ for %
#  __pow__ for **
#  __and__ for &
#  __xor__ for ^
#  __or__ for |
#  Выражение x + y переводится в x.__add__(y),
#  Однако, если x не реализовал __add__, а x и y имеют разные типы, то вызывается y.__radd__(x)

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __truediv__(self, other):
#         line = "=" * len(other.cont)
#         return "\n".join([self.cont, line, other.cont])
#
#
# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(spam / hello)

# TODO: Python также предоставляет волшебные методы для сравнения.
#  __lt__ for <
#  __le__ for <=
#  __eq__ for ==
#  __ne__ for !=
#  __gt__ for >
#  __ge__ for >=
#  Если __ne__ не реализовано, возвращается значение, противоположное __eq__ .
#  Других отношений между другими операторами нет.
#  Можем определить любое пользовательское поведение для перегруженных операторов.
# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __gt__(self, other):
#         for index in range(len(other.cont) + 1):
#             result = other.cont[:index] + " > " + self.cont
#             result += " > " + other.cont[index:]
#             print(result)
#
#
# spam = SpecialString("spam")
# eggs = SpecialString("eggs")
# spam > eggs

# TODO: Есть несколько волшебных способов заставить классы работать как контейнеры.
#  __len__ для len()
#  __getitem__ для индексации
#  __setitem__ для присвоения индексированным значениям
#  __delitem__ для удаления индексированных значений
#  __iter__ для итерации по объектам (например, in для циклов)
#  __contains__ для in
#  Существует множество других волшебных методов, которые мы не будем здесь рассматривать,
#  например __call__ для вызова объектов как функций и __int__ , __str__ и т.п.
#  для преобразования объектов во встроенные типы.
#  Мы переопределили функцию len() для класса VagueList, чтобы она возвращала случайное число.
#  Функция индексирования также возвращает случайный элемент в диапазоне из списка на основе выражения.
# import random
#
#
# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1, 1)]
#
#     def __len__(self):
#         return random.randint(0, len(self.cont) * 2)
#
#
# vague_list = VagueList(["A", "B", "C", "D", "E"])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])

# TODO: Object Lifecycle - Жизненный цикл объекта состоит из его создания, манипулирования и уничтожения.
#  Первым этапом жизненного цикла объекта является определение класса, к которому он принадлежит.
#  Следующий этап — создание экземпляра, когда вызывается __init__ .
#  Память выделяется для хранения экземпляра. Непосредственно перед этим вызывается метод __new__ класса.
#  Обычно это переопределяется только в особых случаях. После этого объект готов к использованию.
#  Затем другой код может взаимодействовать с объектом, вызывая для него функции и получая доступ к его атрибутам.
#  В конце концов, он перестанет использоваться и может быть уничтожен.
#  Когда объект уничтожается, выделенная ему память освобождается и может быть использована для других целей.
#  Уничтожение объекта происходит, когда его счетчик ссылок достигает нуля.
#  Счетчик ссылок — это количество переменных и других элементов, которые ссылаются на объект.
#  Если на него ничего не ссылается (у него счетчик ссылок равен нулю),
#  ничто не может с ним взаимодействовать, поэтому его можно безопасно удалить.
#  В некоторых ситуациях два (или более) объекта могут ссылаться только друг на друга и, следовательно,
#  также могут быть удалены. Оператор del уменьшает счетчик ссылок на объект на единицу,
#  что часто приводит к его удалению. Волшебный метод для оператора del — __del__.
#  Процесс удаления объектов, когда они больше не нужны, называется сборщик мусора .
#  Таким образом, счетчик ссылок на объект увеличивается, когда ему присваивается новое имя или он помещается в
#  контейнер (список, кортеж или словарь). Счетчик ссылок на объект уменьшается, когда он удаляется с помощью del,
#  его ссылка переназначается или его ссылка выходит за пределы области действия.
#  Когда счетчик ссылок на объект достигает нуля, Python автоматически удаляет его.
#  Языки более низкого уровня, такие как C, не имеют такого автоматического управления памятью.
# a = 42  # Create object <42>
# b = a  # Increase ref. count  of <42>
# c = [a]  # Increase ref. count  of <42>
#
# del a  # Decrease ref. count  of <42>
# b = 100  # Decrease ref. count  of <42>
# c[0] = -1  # Decrease ref. count  of <42>

# TODO: Data Hiding - Ключевой частью ООП является инкапсуляция, которая включает в себя упаковку
#  связанных переменных и функций в один простой в использовании объект — экземпляр класса.
#  Родственная концепция — скрытие данных, в которой говорится, что детали реализации класса должны быть скрыты,
#  а для тех, кто хочет использовать класс, должен быть представлен чистый стандартный интерфейс.
#  В других языках программирования это обычно делается с помощью закрытых методов и атрибутов,
#  которые блокируют внешний доступ к определенным методам и атрибутам в классе.
#  Философия Python немного отличается. Часто говорят, что «мы все здесь взрослые по обоюдному согласию», что означает,
#  что вы не должны накладывать произвольные ограничения на доступ к частям класса.
#  Следовательно, нет способов заставить метод или атрибут быть строго закрытым.
#  Однако есть способы отговорить людей от доступа к частям класса, например, обозначив,
#  что это деталь реализации, которую следует использовать на свой страх и риск.
#  Слабо приватные методы и атрибуты имеют один подчеркивание в начале.
#  Это сигнализирует о том, что они являются частными и не должны использоваться внешним кодом.
#  Однако в основном это всего лишь соглашение, которое не препятствует доступу к ним внешнего кода.
#  Его единственный фактический эффект заключается в том, что from module_name import * не будет
#  импортировать переменные, начинающиеся с одного символа подчеркивания.
# class Queue:
#     def __init__(self, contents):
#         self._hiddenlist = list(contents)
#
#     def push(self, value):
#         self._hiddenlist.insert(0, value)
#
#     def pop(self):
#         return self._hiddenlist.pop(-1)
#
#     def __repr__(self):
#         return "Queue({})".format(self._hiddenlist)
#
#
# # TODO: В приведенном выше коде атрибут _hiddenlist помечен как приватный, но к нему по-прежнему можно
# #  получить доступ во внешнем коде. Магический метод __repr__ используется для строкового представления экземпляра.
#
# queue = Queue([1, 2, 3])
# print(queue)
# queue.push(0)
# print(queue)
# queue.pop()
# print(queue)
# print(queue._hiddenlist)

# TODO: Строгие частные методы и атрибуты имеют двойное подчеркивание в начале своего имени.
#  Это приводит к тому, что их имена искажаются, а это означает, что к ним нельзя получить доступ извне класса.
#  Цель этого не в том, чтобы гарантировать их приватность, а во избежание ошибок,
#  если есть подклассы, которые имеют методы или атрибуты с теми же именами.
#  Доступ к методам с измененным именем по-прежнему можно получить извне, но под другим именем.
#  К методу __privatemethod класса Spam можно было получить доступ извне с помощью _Spam__privatemethod.
#  По сути, Python защищает эти члены, внутренне изменяя имя, чтобы оно включало имя класса.
# class Spam:
#     __egg = 7
#
#     def print_egg(self):
#         print(self.__egg)
#
#
# s = Spam()
# s.print_egg()
# print(s._Spam__egg)
# print(s.__egg)

# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance
#
#     def __repr__(self):
#         return f'Account Balance: {self._balance}'
#
#     def deposit(self, amount):
#         self._balance += amount
#
#
# acc = BankAccount(0)
# acc.deposit(int(input()))
# print(acc)

# TODO: Class Methods (Методы класса).
#  Методы объектов, которые мы рассмотрели до сих пор, вызываются экземпляром класса,
#  который затем передается параметру self метода.
#  Методы класса бывают разные - их вызывает класс, который передается в параметр cls метода.
#  Обычно они используются в фабричных методах, которые создают экземпляр класса с использованием параметров,
#  отличных от тех, которые обычно передаются конструктору класса.
#  Методы класса отмечены декоратором classmethod.
#  new_square — это метод класса, который вызывается в классе, а не в экземпляре класса.
#  Он возвращает новый объект класса cls.
#  Технически параметры self и cls — это просто соглашения; их можно поменять на что угодно.
#  Тем не менее, им следуют повсеместно, поэтому разумно придерживаться их.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     @classmethod
#     def calculate_area_square(cls, side_length):
#         return cls(side_length, side_length)
#
#
# square = Rectangle.calculate_area_square(5)
# print(square.calculate_area())
#
# rectangle = Rectangle(4, 5)
# print(rectangle.calculate_area())

# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def sayHi(cls):
#         return "Hi"
#
#
# person = Person.sayHi()
# print(person)

# TODO: Static Methods - Статические методы аналогичны методам класса, за исключением того, что они не получают
#  никаких дополнительных аргументов; они идентичны обычным функциям, принадлежащим классу.
#  Они отмечены декоратором staticmethod.
#  Статические методы ведут себя как обычные функции, за исключением того, что их можно вызывать из экземпляра класса.
# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#
#     @staticmethod
#     def validate_topping(topping):
#         if topping == "pineapple":
#             raise ValueError("No pineapples!")
#         else:
#             return True
#
#
# ingredients = ["cheese", "onions", "spam"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#     pizza = Pizza(ingredients)
#
# topping_check = Pizza.validate_topping("cheese")
# print(topping_check)

# class Calculator:
#     @staticmethod
#     def add(n1, n2):
#         return n1 + n2
#
#
# n1 = int(input())
# n2 = int(input())
#
# print(Calculator.add(n1, n2))

# TODO: Properties - Свойства предоставляют способ настройки доступа к атрибутам экземпляра.
#  Они создаются путем размещения декоратора свойства над методом, что означает, что при доступе
#  к атрибуту экземпляра с тем же именем, что и у метода, вместо этого будет вызываться метод.
#  Одно из распространенных применений свойства — сделать атрибут доступным только для чтения.
# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#
#     @property
#     def pineapple_allowed(self):
#         return False
#
#
# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# # pizza.pineapple_allowed = True

# class Person:
#
#     def __init__(self, age):
#         self.age = int(age)
#
#
# @property
# def isAdult(self):
#     if self.age > 18:
#         return True
#     else:
#         return False
#
#
# human = Person(27).age
# boy = Person(16).age
# print(human)
# print(boy)

# TODO: Свойства также можно установить, определив функции setter/getter (установки/получения).
#  Функция установки устанавливает значение соответствующего свойства.
#  Геттер получает значение.
#  Чтобы определить setter, вам нужно использовать декоратор с тем же именем,
#  что и у свойства, за которым следует точка и ключевое слово setter.
#  То же самое относится к определению функций получения.
# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#         self._pineapple_allowed = False
#
#     @property
#     def pineapple_allowed(self):
#         return self._pineapple_allowed
#
#     @pineapple_allowed.setter
#     def pineapple_allowed(self, value):
#         if value:
#             password = input("Enter the password: ")
#             if password == "Sw0rdf1sh!":
#                 self._pineapple_allowed = value
#             else:
#                 raise ValueError("Alert! Intruder!")
#
#
# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)

# class Number:
#     def __init__(self, num):
#         self.value = num
#
#     @property
#     def isEven(self):
#         if self.value % 2 == 0:
#             return True
#         else:
#             return False
#
#
# x = Number(int(input()))
# print(x.isEven)

# TODO: A Simple Game. Объектная ориентация очень полезна при управлении различными объектами и их отношениями.
#  Это особенно полезно, когда вы разрабатываете игры с разными персонажами и функциями.
#  Давайте рассмотрим пример проекта, который показывает, как классы используются в разработке игр.
#  Разрабатываемая игра представляет собой старомодную текстовую приключенческую игру.
#  Ниже приведена функция обработки ввода и простой синтаксический анализ.
# def get_input():
#     command = input(": ").split()
#     verb_word = command[0]
#     if verb_word in verb_dict:
#         verb = verb_dict[verb_word]
#     else:
#         print(f'Unknown verb {verb_word}')
#         return
#
#     if len(command) >= 2:
#         noun_word = command[1]
#         print(verb(noun_word))
#     else:
#         print(verb("nothing"))
#
#
# def say(noun):
#     return f'You said "{noun}"'
#
#
# def hi(word):
#     word = 'Hello!'
#     return word
#
#
# verb_dict = {
#     "say": say,
#     "Hi": hi,
#     "HI": hi,
#     "hello": hi,
#     "Hello": hi,
#     "Hello!": hi,
#     "HELLO": hi,
#
# }
#
# while True:
#     get_input()

# TODO: Следующим шагом будет использование классов для представления игровых объектов.
#  Мы создали класс Goblin, который наследуется от класса GameObjects.
#  Мы также создали новую функцию exam, которая возвращает описание объектов.
#  Теперь мы можем добавить в наш словарь новый глагол «исследовать» и попробовать его!
# class GameObject:
#     class_name = ""
#     desc = ""
#     objects = {}
#
#     def __init__(self, name):
#         self.name = name
#         GameObject.objects[self.class_name] = self
#
#     def get_desc(self):
#         return self.class_name + "\n" + self.desc
#
#
# class Goblin(GameObject):
#     def __init__(self, name):
#         self.class_name = "goblin"
#         self.health = 3
#         self._desc = " A foul creature"
#         super().__init__(name)
#
#     @property
#     def desc(self):
#         if self.health >= 3:
#             return self._desc
#         elif self.health == 2:
#             health_line = "It has a wound on its knee."
#         elif self.health == 1:
#             health_line = "Its left arm has been cut off!"
#         elif self.health <= 0:
#             health_line = "It is dead."
#         return self._desc + "\n" + health_line
#
#     @desc.setter
#     def desc(self, value):
#         self._desc = value
#
#
# def hit(noun):
#     if noun in GameObject.objects:
#         thing = GameObject.objects[noun]
#         if type(thing) == Goblin:
#             thing.health = thing.health - 1
#             if thing.health <= 0:
#                 msg = "You killed the goblin!"
#             else:
#                 msg = f"You hit the {thing.class_name}"
#     else:
#         msg = f"There is no {noun} here."
#     return msg
#
#
# goblin = Goblin("Gobbly")
#
#
# def examine(noun):
#     if noun in GameObject.objects:
#         return GameObject.objects[noun].get_desc()
#     else:
#         return f"There is no {noun} here."
#
#
# def get_input():
#     command = input(": ").split()
#     verb_word = command[0]
#     if verb_word in verb_dict:
#         verb = verb_dict[verb_word]
#     else:
#         print(f'Unknown verb {verb_word}')
#         return
#
#     if len(command) >= 2:
#         noun_word = command[1]
#         print(verb(noun_word))
#     else:
#         print(verb("nothing"))
#
#
# def say(noun):
#     return f'You said "{noun}"'
#
#
# verb_dict = {
#     "say": say,
#     "examine": examine,
# }
# while True:
#     get_input()


# class Test:
#     __egg = 7
#
#
# t = Test()
# print(t._Test__egg)


# class Person:
#
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#
# richi = Person('Ричи')
# print(richi.name)

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f'{self.name} ({self.capacity}L)'

    def __add__(self, other):
        self.name += f'&{other.name}'
        self.capacity += other.capacity
        return self.__str__


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)
c = Juice('lemon', 0.5)
result_a_b = a.__add__(b)()
result_b_c = b.__add__(c)()
result_a_b_c = a.__add__(c)()
result_c_a_b_c = c.__add__(a)()
print(result_a_b)
print(result_b_c)
print(result_a_b_c)
print(result_c_a_b_c)



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
