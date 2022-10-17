SELECT name
FROM films
WHERE year >= 2010 AND production = 'Marvel Studios'
ORDER BY name 

SELECT teamname, country
FROM teams
WHERE country IN ('Spain', 'Germany', 'England')
ORDER BY teamname 

SELECT CONCAT(firstname,' ',lastname) AS fullname, (salary * 12) + (experience * 500) AS total
FROM staff
ORDER BY total 

SELECT AVG(score)
FROM sam_grades
WHERE semester = 1

SELECT *
FROM Foods
WHERE fatpercentage < ( SELECT AVG(fatpercentage) FROM Foods)

SELECT *
FROM desserts
WHERE name LIKE '%Chocolate%'

SELECT students.id, students.firstname, students.lastname, teachers.lastname AS teacher
FROM students, teachers
WHERE (students.teacherid = teachers.id)
ORDER BY students.id 

SELECT products.productname, products.price, categories.categoryname
FROM products INNER JOIN categories ON products.categoryid = categories.id

SELECT * FROM NorwayChess 
UNION 
SELECT * FROM TataSteel 
ORDER BY rating DESC

INSERT INTO Garage (id, make, model, prodyear) VALUES 
(6, 'Mercedes-Benz', 'G 63', 2020),
(7, 'Porsche', 'Panamera', 2020);
SELECT *
FROM Garage

DELETE FROM products 
WHERE expiredate < 1;
SELECT * FROM products

CREATE TABLE leaderboard(place int, nickname VARCHAR(128), rating int);
INSERT INTO leaderboard (place , nickname, rating) 
VALUES 
(1, 'Predator', 9500),
(2, 'JohnWar', 9300),
(3, 'NightWarrior', 8900);
SELECT * FROM leaderboard

