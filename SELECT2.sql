SELECT
	id 
	, SURNAME AS ФАМИЛИЯ
	, NAME AS ИМЯ
	, PATRONYMIC AS Отчество
	, CITY AS Местоположение
	, gender AS пол
FROM
	TUTOR
WHERE
	PATRONYMIC = "Николаевич"
ORDER BY
	id ASC
	, NAME DESC
