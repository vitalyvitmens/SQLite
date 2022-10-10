SELECT 
	genres.name AS ЖАНР
	, SURNAME AS ФАМИЛИЯ
	, TUTOR.NAME AS ИМЯ
	, CITY AS МЕСТОПОЛОЖЕНИЕ
FROM
	genres
	LEFT JOIN TUTOR
		ON genres.GenreId = TUTOR.GenreId
WHERE 
	genres.Name IN('Rock', 'Metal', 'Hip Hop/Rap', 'Шансон')
	OR TUTOR.SURNAME Like ('Ляли%')
ORDER BY
	SURNAME 
LIMIT 10
