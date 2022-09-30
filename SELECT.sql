SELECT -- после слова SELECT мы описываем что конкретно мы выбираем (перечисление колонок, какие то операции над ними)
	id 
	, SURNAME AS ФАМИЛИЯ
	, NAME AS ИМЯ
	, CITY AS Местоположение
	, gender AS пол
FROM -- после FROM мы описываем откуда мы выбираем конкретное название одной таблицы в данном случае TUTOR, 
     -- можно перечислять несколько таблиц и взаимодействовать между ними
	TUTOR
WHERE -- где (WHERE), условие выборки, что бы выбор попал в финальную выборку это условие должно выполняться
	(id > 4
	AND id < 11)
	OR CITY = "Минск"
    OR gender = "M"
ORDER BY -- сортировка: ASC с меньшего на большее, DESC с последнего к первому 
	id ASC
	, NAME DESC
LIMIT 10 -- говорим что максимально должно выдаться не больше 10 значений 
OFFSET 1 -- OFFSET 1 говорит об 1 отступе (пропустив 1 значение)