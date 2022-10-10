SELECT 
	id AS id
	, SURNAME AS ФАМИЛИЯ
	, name AS ИМЯ
	, CITY AS МЕСТОНАХОЖДЕНИЕ
	--, GenreId AS genre_id
FROM
	TUTOR
WHERE 
	gender = "M"
	AND (NAME IN ("Александр", "Николай") 
	OR NAME like "%талий") --остерегайтесь использовать like при большом объеме данных!!!
ORDER BY id DESC
LIMIT 15
