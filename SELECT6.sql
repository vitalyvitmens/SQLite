SELECT 
	*
FROM
	TUTOR
WHERE 
	--gender = "M"
	NAME IN ("Александр", "Николай", "Екатерина", "Ольга") 
ORDER BY id DESC
LIMIT 15
