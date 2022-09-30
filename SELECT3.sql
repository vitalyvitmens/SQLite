SELECT
	id 
	, SURNAME AS ФАМИЛИЯ
	, NAME AS ИМЯ
	, PATRONYMIC AS Отчество
	, SALARY AS ЗП
	, CITY AS Местоположение
	, gender AS пол
FROM
	TUTOR
WHERE
	SALARY > 4000
ORDER BY
	SALARY DESC
