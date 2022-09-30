SELECT
	id * 9 + id
	, SURNAME AS ФАМИЛИЯ
	, NAME AS ИМЯ
	, CITY AS Местоположение
	, gender AS пол
FROM
	TUTOR
WHERE
	(id > 0
	AND id < 16)
ORDER BY
	id ASC
	, NAME DESC
LIMIT 100
OFFSET 0