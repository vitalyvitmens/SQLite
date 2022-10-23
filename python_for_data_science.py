"""
Python for Data Science:
Python широко используется в науке о данных и имеет надежный набор мощных инструментов для обмена данными.
В этом курсе вы узнаете о различных библиотеках Python, используемых для обработки и визуализации данных,
таких как numpy, pandas, matplotlib и других.
"""
# TODO: Добро пожаловать на наш курс Python для науки о данных!
#  В этом курсе вы узнаете о самых популярных библиотеках Python,
#  используемых в науке о данных: numpy, pandas и matplotlib .
#  Мы будем решать реальные проблемы, решать задачи, анализировать реальные данные и визуализировать полученные данные!
#  Если вы не знакомы с базовым синтаксисом Python,
#  лучше сначала пройти наши курсы Python для начинающих и Структуры данных Python, прежде чем начинать этот.

# TODO: Python — язык программирования №1 для Data Science, и на то есть веские причины:
#  — Python легко освоить.
#  - Синтаксис легко читать и понимать.
#  - Есть много полезных библиотек для выполнения вычислений и других операций.
#  Как правило, код Python также намного короче по сравнению с другими языками программирования.

# TODO: Statistics (Статистика)
#  Наука о данных использует различные техники и методы для извлечения знаний и статистики из данных.
#  Давайте сначала погрузимся в некоторые основы статистики.
#  Эти концепции составляют основные строительные блоки анализа данных.
#  В качестве примера набора данных рассмотрим цены на группу товаров:
#  [18, 24, 67, 55, 42, 14, 19, 26, 33]
#  Данный набор данных включает цены на 9 товаров. Среднее значение — это среднее значение набора данных.
#  Мы можем рассчитать его, сложив все цены вместе и разделив на количество продуктов: среднее значение = 298/9 = 33,1.
#  Обратите внимание, что среднее значение обычно не является частью нашего набора данных.
# from statistics import mean
#
# x = [2, 4, 6, 8]
# a = sum(x) / len(x)
# b = mean(x)
# print(round(a, 1))
# print(b)

# TODO: Median (медиана)
#  Еще одна полезная концепция — медиана: среднее значение упорядоченного набора данных.
#  Чтобы вычислить медиану для нашего набора данных о ценах, давайте сначала упорядочим его в порядке возрастания:
#  [14, 18, 19, 24, 26, 33, 42, 55, 67]
#  Медиана равна 26, так как это среднее значение.
#  Если бы в нашем наборе данных было четное количество значений,
#  мы бы взяли два значения посередине и вычислили их среднее значение.
#  Медиана обычно более полезна, чем среднее значение.
#  Это связано с тем, что среднее значение может сильно различаться из-за того,
#  что одно значение намного больше или меньше других.
#  Среднее значение и медиана называются показателями центральной тенденции,
#  поскольку они описывают, где находится центр наших данных.
# from statistics import median
#
# x = [2, 2, 3, 5, 8, 9]
# print(median(x))

# TODO: ЗАДАЧА: Количество прививок
#  У нас есть отчет о количестве прививок от гриппа в классе из 20 человек.
#  Он имеет следующие числа:
#  - никогда: 5
#  - единожды: 8
#  - дважды: 4
#  - трижды: 3
#  Каково среднее количество раз, когда эти люди были вакцинированы? Выведите результат с помощью оператора print().
#  Подсказка: подумайте о данных следующим образом: они содержат 20 значений,
#  каждое из которых представляет количество прививок, сделанных соответствующему человеку.
# vac_nums = [0, 0, 0, 0, 0,
#             1, 1, 1, 1, 1, 1, 1, 1,
#             2, 2, 2, 2,
#             3, 3, 3
#             ]
# print(sum(vac_nums) / len(vac_nums))

# TODO: Standard Deviation (Стандартное отклонение)
#  Стандартное отклонение — это мера того, насколько разбросаны наши данные.
#  Чтобы вычислить его, нам сначала нужно вычислить значение, называемое дисперсией:
#  это среднее значение квадратов отличий от среднего.
#  Итак, для наших ценовых данных:
#  [14, 18, 19, 24, 26, 33, 42, 55, 67]
#  среднее значение 33,1.
#  Чтобы вычислить дисперсию, мы берем разницу между каждым значением и средним значением, возводим ее в квадрат, а
#  затем усредняем результат:
#  можно проверить, какие возрасты находятся в пределах одного стандартного отклонения (17,1)
#  от среднего (33,1) - от (33,1-17,1) до (33,1+17,1):
#  [14, 18, 19, 24, 26, 33, 42, 55, 67]
#  Как видите, 6 значений из 9 находятся в этом диапазоне.
#  Низкое стандартное отклонение указывает на то, что значения имеют тенденцию быть близкими к среднему значению набора,
#  в то время как высокое стандартное отклонение указывает на то, что значения разбросаны по более широкому диапазону.
# from statistics import *
#
# x = [2, 2, 2, 2]
# mean = round(mean(x), 1)
# print(mean)
# dispersions = []
# for i in x:
#     a = round((i - mean), 1)
#     dispersions.append(a)
# print(dispersions)
# dispersion = []
# for i in dispersions:
#     a = round((i ** 2))
#     dispersion.append(a)
# print(dispersion)
# disper = (sum(dispersion) / len(dispersion)) ** 0.5
# print(round(disper, 1))
# b = []
# for i in x:
#     if mean - disper <= i <= mean + disper:
#         b.append(i)
# print(b)
# print(len(b))

# TODO: Статистика
#  Мы узнали, как рассчитать основную сводную статистику для набора данных:
#  mean (среднее значение): среднее значение.
#  median (медиана): медианное значение.
#  standard deviation (стандартное отклонение): мера разброса.
#  Эти статистические данные предоставляют информацию о вашем наборе данных и помогают понять,
#  где находятся значения ваших данных и как они распределяются.
#  Python предоставляет библиотеки, которые вычисляют для вас сводную статистику. О них мы узнаем на следующих уроках.

# TODO: ЗАДАЧА: Количество прививок
#  Использование того же набора данных о прививках,
#  который включает количество раз, когда люди получали вакцину против гриппа.
#  Набор данных содержит следующие числа:
#  - никогда: 5
#  - единожды: 8
#  - дважды: 4
#  - трижды: 3
#  Рассчитайте и выведите дисперсию.
#  Вскоре мы узнаем о более простых способах расчета дисперсии и других сводных статистических данных с помощью Python.
#  А пока используйте код Python для вычисления результата с помощью соответствующего уравнения.
#  Подсказка : Дисперсия – это среднее квадратов отличий от среднего.
# import numpy as np
#
# vac_nums = [0, 0, 0, 0, 0,
#             1, 1, 1, 1, 1, 1, 1, 1,
#             2, 2, 2, 2,
#             3, 3, 3
#             ]
# a = np.array(vac_nums)
# mean = np.sum(a) / a.size
# v = np.sum((a - mean) ** 2) / a.size
# print(v)

# vac_nums = [0, 0, 0, 0, 0,
#             1, 1, 1, 1, 1, 1, 1, 1,
#             2, 2, 2, 2,
#             3, 3, 3
#             ]
# mean = sum(vac_nums) / len(vac_nums)
# v = []
# for i in vac_nums:
#     v.append((i - mean) ** 2)
# v1 = sum(v) / len(v)
# print(v)
# print(v1)

# TODO: ЗАДАЧА: Баскетболисты
#  Данный код включает в себя список роста для различных баскетболистов.
#  Вам нужно рассчитать и вывести, сколько игроков находится в диапазоне одного стандартного отклонения от среднего.
#  Выведите результат с помощью оператора печати.
# players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
# mean = sum(players) / len(players)
# dispersions = []
# for i in players:
#     a = i - mean
#     dispersions.append(a)
# dispersion = []
# for i in dispersions:
#     a = i ** 2
#     dispersion.append(a)
# disper = (sum(dispersion) / len(dispersion)) ** 0.5
# b = []
# for i in players:
#     if mean - disper <= i <= mean + disper:
#         b.append(i)
# print(len(b))

# TODO: NumPy (Numerical Python)(Числовой Python) — это библиотека Python, используемая для работы с числовыми данными.
#  NumPy включает в себя функции и структуры данных, которые могут выполнять широкий спектр математических операций.
#  Чтобы начать использовать NumPy, нам сначала нужно его импортировать:
#  импортировать numpy как np
#  import numpy as np
#  np — наиболее распространенное имя, используемое для импорта numpy.

# TODO: NumPy Array Массив NumPy
#  В Python списки используются для хранения данных.
#  NumPy предоставляет структуру массива для выполнения операций с данными.
#  Массивы NumPy быстрее и компактнее списков. Массив NumPy можно создать с помощью функции np.array(),
#  предоставив ей список в качестве аргумента:
#  x = np.array([1, 2, 3, 4])
#  Теперь x — это массив NumPy, содержащий 4 значения.
#  Мы можем получить доступ к его элементам, используя их индексы, которые начинаются с 0:
#  Массивы NumPy являются гомогенными, то есть они могут содержать только один тип данных,
#  тогда как списки могут содержать несколько разных типов данных.
# import numpy as np
#
# x = np.array([1, 2, 3, 4])
# print(x[0])
# mean = np.sum(x) / x.size
# print(mean)
# v = np.sum((x - mean) ** 2) / x.size
# print(v)

# TODO: NumPy Arrays - Массивы NumPy часто называют ndarrays, что означает "N-dimensional array" (N-мерный массив),
#  поскольку они могут иметь несколько измерений.
#  Например:
#  x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#  print(x[1][2])
#  Это создаст двумерный массив, который имеет 3 столбца и 3 строки, и выведет значение во 2-й строке и 3-м столбце.
#  Массивы имеют свойства, доступ к которым можно получить с помощью точки
#       .ndim возвращает количество измерений массива
#       .size возвращает общее количество элементов массива
#       .shape возвращает кортеж целых чисел, указывающих количество элементов, хранящихся в каждом измерении массива.
#  Например:
#  x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#  print(x.ndim)  # 2
#  print(x.size)  # 9
#  print(x.shape)  # (3, 3)
#  Итак, массив в нашем примере имеет 2 измерения, 9 элементов и представляет собой матрицу 3x3 (3 строки и 3 столбца).
# import numpy as np
#
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(x[1][2])
# vac_nums = np.array([0, 0, 1, 0, 1,
#                      0, 0, 0, 1, 1,
#                      1, 0, 0, 0, 0,
#                      0, 1, 0, 0, 1,
#                      1, 1, 0, 1, 0,
#                      ])
# print(vac_nums.ndim)
# print(vac_nums.size)
# print(vac_nums.shape)

# TODO: Массивы NumPy
#  Мы можем добавлять, удалять и сортировать массив с помощью функций np.append(), np.delete() и np.sort().
#  Например:
# import numpy as np
#
# x = np.array([2, 3, 1])
#
# x = np.append(x, 4)
# x = np.delete(x, 0)
# x = np.sort(x)
# print(x)

# TODO: np.arange() позволяет создать массив, содержащий диапазон равномерно расположенных интервалов
#  (аналогично диапазону Python):
#  Это создаст массив [2, 5, 8]
# x = np.arange(2, 10, 3)
# print(x)

# TODO: ЗАДАЧА: Квадратные метры
#  Вам дан массив, содержащий данные о площади домов на определенной улице.
#  На этой улице только что построили новый дом.
#  Измените свою программу, чтобы она принимала новое значение дома в качестве входных данных,
#  добавляла его к массиву и выводила массив, отсортированный в порядке возрастания.
#  Используйте оператор печати для вывода объекта массива.
# import numpy as np
#
# data = np.array([1000, 2500, 1400, 1800, 900, 4200, 2200, 1900, 3500])
# data = np.append(data, int(input()))
# data = np.sort(data)
# print(data)

# TODO: Reshape (Изменить форму)
#  Напомним, что фигура относится к количеству строк и столбцов в массиве. Например, рассмотрим следующий массив:
#      import numpy as np
#      x = np.arange(1, 7)
#      print(x)
# TODO: Это одномерный массив, содержащий 6 элементов.
#  NumPy позволяет нам изменять форму наших массивов с помощью функции reshape().
#  Например, мы можем изменить наш одномерный массив на массив с 3 строками и 2 столбцами:
#      import numpy as np
#      x = np.arange(1, 7)
#      z = x.reshape(3, 2)
#      print(z)
# TODO: Когда вы используете метод изменения формы, массив, который вы хотите создать,
#  должен иметь то же количество элементов, что и исходный массив.

# TODO: Reshape также может сделать обратное: взять 2-мерный массив и сделать из него 1-мерный массив:
#  В результате получается плоский массив, содержащий 6 элементов.
#  Того же результата можно добиться с помощью функции flatten().
# import numpy as np
#
# x = np.array([[1, 2], [3, 4], [5, 6]])
# z = x.reshape(6)
# print(z)
#
# x = np.arange(1, 8, 3)
# z = x.reshape(3, 1)
# print(z[1][0])

# TODO: ЗАДАЧА: Места в театре
#  Вам дан массив, представляющий заполняемость мест в кинотеатре.
#  Место, отмеченное цифрой 1, занято, а место, отмеченное цифрой 0, означает, что место свободно.
#  Однако массив плоский и одномерный. Преобразуйте его в двумерный массив, представляющий ряды сидений.
#  В каждом ряду театра по 5 мест, всего 30 мест.
#  Придайте массиву соответствующую форму и выведите строку с заданным индексом,
#  который берется из пользовательского ввода.
#  Индекс строки берется из пользовательского ввода в данном коде.
# import numpy as np
#
# data = np.array([1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0])
# row = int(input())
# data_new = data.reshape(6, 5)
# print(data_new[row])

# TODO: Indexing and Slicing - Индексирование и нарезка
#  Массивы NumPy можно индексировать и нарезать так же, как списки Python.
#  Отрицательные индексы считаются с конца массива, поэтому [-3:] приведет к последним 3 элементам.
#  Например:
# import numpy as np
#
# x = np.arange(1, 10)
# print(x)
# print(x[0:2])
# print(x[5:])
# print(x[:2])
# print(x[-3:])

# TODO: Conditions - Условия
#  Вы можете указать условие в качестве индекса для выбора элементов, которые удовлетворяют заданному условию.
#  Например, давайте выберем элементы меньше 4:
# import numpy as np
#
# x = np.arange(1, 10)
# print(x[x < 4])
# TODO: Условия можно комбинировать с помощью знаков & (и) и | (или) операторы.
#  Например, возьмем четные числа больше 5:
# import numpy as np
#
# x = np.arange(1, 10)
# print(x[(x > 5) & (x % 2 == 0)])
# y = (x > 5) & (x % 2 == 0)
# TODO: Условие также может быть присвоено переменной, которая будет массивом логических значений, показывающих,
#  соответствуют ли значения в массиве условию:
# import numpy as np
#
# x = np.arange(1, 10)
# y = (x > 5) & (x % 2 == 0)
# print(x[y])

# import numpy as np
#
# x = np.array([11, 42, 8, 5, 18])
# z = x[x > 15]
# print(z.size)

# TODO: ЗАДАЧА: Multiples of 3 & 5 (Кратность 3 и 5)
#  Вам дается задание найти все целые числа меньше 100, которые кратны как 3, так и 5.
#  Создайте массив чисел до 100, кратных как 3, так и 5, и выведите его.
#  Вы можете использовать оператор по модулю %, чтобы проверить, является ли число кратным другому числу.
# import numpy as np
# x = np.arange(1, 100)
# y = (x < 100) & (x % 3 == 0) & (x % 5 == 0)
# print(x[y])

# TODO: Operations - Операции
#  С массивами легко выполнять основные математические операции.
#  Например, чтобы найти сумму всех элементов, мы используем функцию sum():
# import numpy as np
#
# x = np.arange(1, 10)
# print(x.sum())
# TODO: Точно так же min() и max() можно использовать для получения наименьшего и наибольшего элементов.
#  Мы также можем выполнять операции между массивом и одним числом. Например, мы можем умножить все элементы на 2:
#  Так просто, как, что! Возьмите свой массив и выполните с ним любую операцию, которую хотите!
#  NumPy понимает, что данная операция должна выполняться с каждым элементом. Это называется трансляция.
# import numpy as np
#
# x = np.arange(1, 10)
# print(x)
# print(sum(x))
# y = x * 2
# print(y)
# print(sum(y))

# TODO: Statistics (Статистика)
#  Помните сводную статистику, которую мы изучили в предыдущем модуле?
#  К ним относятся:
#  - mean (среднее значение),
#  - median (медиана),
#  - variance (дисперсия),
#  - standard deviation (стандартное отклонение).
#  Массивы NumPy имеют встроенные функции для возврата этих значений.
#  Как видите, NumPy предоставляет множество полезных функций для выполнения обычных операций с массивами.
# import numpy as np
#
# x = np.array([14, 18, 19, 24, 26, 33, 42, 55, 67])
#
# print(np.mean(x))
# print(np.median(x))
# print(np.var(x))
# print(np.std(x))

# TODO: ЗАДАЧА: Ежедневные инфекции
#  Данный массив представляет ежедневное количество заражений за 30 дней.
#  Узнайте, на сколько дней превысило среднее число заражений.
#  Создайте условие и выведите размер результирующего массива.
# import numpy as np
#
# data = np.array(
#     [120, 98, 150, 65, 42, 100, 190, 220, 140, 110, 88, 89, 100, 120, 50, 180, 155, 42, 89, 77, 200, 190, 125, 98, 77,
#      40, 39, 59, 30, 67])
# mean = np.mean(data)
# print(data[data > 105].size)

# import numpy as np
#
# x = np.arange(3, 9)
# z = x.reshape(2, 3)
# print(z[1][1])

# import numpy as np
#
# x = np.arange(1, 5)
# x = x * 2
# print(x[:3].sum())

# TODO: ЗАДАЧА: Цены на дома
#  Вам дан массив, представляющий цены на жилье.
#  Вычислите и выведите процент домов, которые находятся в пределах одного стандартного отклонения от среднего значения.
#  Чтобы вычислить процент, разделите количество домов, удовлетворяющих условию,
#  на общее количество домов и умножьте результат на 100.
# import numpy as np
#
# data = np.array(
#     [150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000,
#      150000, 280000])
# mean = np.mean(data)
# # print(mean)
# std = np.std(data)
# # print(std)
# lens = data[(data > mean - std) & (data < mean + std)]
# # print(lens)
# percent = (lens.size / data.size) * 100
# print(percent)

# TODO: What is Pandas? Что такое Панды?
#  Pandas — одна из самых популярных библиотек для обработки данных в Python.
#  Простой в использовании, он построен на основе NumPy и имеет много общих функций и свойств.
#  C Pandas вы можете читать и извлекать данные из файлов, преобразовывать и анализировать их,
#  рассчитывать статистику и корреляции и многое другое!
#  Чтобы начать использовать pandas, нам нужно сначала импортировать его:
#  import pandas as pd
#  pd — это обычное короткое имя, используемое при импорте библиотеки.
#  Pandas происходит от термина «панельные данные», эконометрического термина для наборов данных,
#  которые включают наблюдения за несколькими периодами времени для одних и тех же людей.

# TODO: Series & DataFrames (Серии и кадры данных)
#  Двумя основными компонентами pandas являются Series и DataFrame.
#  Серия — это, по сути, столбец, а DataFrame — это многомерная таблица, состоящая из набора серий.
#  Например, следующий DataFrame состоит из двух серий, возраста и роста. См рис. файл: DataFrame.png
#  Вы можете думать о Series как об одномерном массиве, а DataFrame — как о многомерном массиве.

# TODO: DataFrames (кадры данных)
#  Прежде чем работать с реальными данными, давайте сначала создадим DataFrame вручную, чтобы изучить его функции.
#  Самый простой способ создать DataFrame — использовать словарь:
#  data = {
#    'ages': [14, 18, 24, 42],
#    'heights': [165, 180, 176, 184]
#  }
#  Каждый ключ — это столбец, а значение — это массив, представляющий данные для этого столбца.
#  Теперь мы можем передать этот словарь в конструктор DataFrame:
#  Запустите код, чтобы увидеть полученный DataFrame.
# import pandas as pd
#
# data = {
#     'ages': [14, 18, 24, 42],
#     'heights': [165, 180, 176, 184]
# }
#
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
#
# x = {
#     'a': [1, 2],
#     'b': [3, 4],
#     'c': [5, 6]
# }
# df = pd.DataFrame(x)
# print(df)

# TODO: кадры данных
#  DataFrame автоматически создает числовой индекс для каждой строки.
#  Мы можем указать собственный индекс при создании DataFrame:
# import pandas as pd
#
# data = {
#     'ages': [14, 18, 24, 42],
#     'heights': [165, 180, 176, 184]
# }
#
# df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
# print(df)
# TODO: Теперь мы можем получить доступ к строке, используя ее индекс и функцию loc[]:
#  Это выведет строку, соответствующую индексу «Боб».
#  Обратите внимание, что loc использует квадратные скобки для указания индекса.
# import pandas as pd
#
# data = {
#     'ages': [14, 18, 24, 42],
#     'heights': [165, 180, 176, 184]
# }
#
# df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
# print(df.loc["Bob"])

# TODO: ЗАДАЧА: Поиск контактов
#  Вам дан словарь с именами и номерами людей.
#  Вам нужно создать DataFrame из словаря и добавить к нему индекс, который должен быть значениями имени.
#  Затем возьмите имя из пользовательского ввода и выведите строку в DataFrame, которая соответствует этой строке.
#  Использовать . loc , чтобы найти указанную строку.
# import pandas as pd
#
# data = {
#     'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
#     'number': ['1234', '5678', '2222', '1111', '0909']
# }
# df = pd.DataFrame(data, index=['James', 'Billy', 'Bob', 'Amy', 'Tom'])
# print(df.loc[input()])
