SELECT 
	ge.name AS ЖАНР
	, SURNAME AS ФАМИЛИЯ
	, tu.NAME AS ИМЯ
	, CITY AS МЕСТОПОЛОЖЕНИЕ
FROM
	genres AS ge
	LEFT JOIN TUTOR AS tu
		ON ge.GenreId = tu.GenreId
WHERE 
	ge.Name IN('Rock', 'Metal', 'Hip Hop/Rap', 'Шансон')
	OR tu.SURNAME Like ('Ляли%')
ORDER BY
	SURNAME 
LIMIT 10
