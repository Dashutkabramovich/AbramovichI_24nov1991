БД “Грибы”

Table 1: mushrooms (Грибы)

Columns:
o	mushroom_id (int, primary key)
o	name (varchar)
o	description (text)
o	season (varchar)
o	edible (boolean)
o	category_id (int, foreign key)
o	primary_region_id (int, foreign key)

Table 2: categories (Категории)
Columns:
o	category_id (int, primary key)
o	name (varchar)
o	description (varchar)

Table 3: regions (Регионы сбора грибов)
Columns:
o	region_id (int, primary key)
o	name (varchar)
o	description (text)
o	size (decimal)

Связи таблиц:
•	Таблица грибов (mushrooms) имеет внешний ключ (category_id), который связывает ее с таблицей категорий (categories). 
Это отношение указывает на категорию каждого гриба.
•	Таблица грибов (mushrooms) имеет внешний ключ (primary_region_id), который связывает ее с таблицей регион сбора грибов (regions).
Эта связь указывает место, где лучше всего собирать каждый гриб.

Составьте следующие запросы:

1.	Выведите все уникальные регионы сбора грибов.

SELECT DISTINCT name
FROM regions;

    2.  Выведите название, сезон сбора и съедобность грибов, которые относятся к категории “Трубчатые”.

SELECT mushrooms.name, mushrooms.season, mushrooms.edible
FROM mushrooms
JOIN categories ON mushrooms.category_id = categories.category_id
WHERE categories.name = 'Трубчатые';

3. Посчитайте количество грибов для каждой категории. Выведите название категории и количество в порядке убывания.

SELECT c.name AS category_name, COUNT(m.mushroom_id) AS mushroom_count
FROM mushrooms m
JOIN categories c ON m.category_id = c.category_id
GROUP BY c.name
ORDER BY mushroom_count DESC;

4. Выведите название и описание съедобных грибов, которые лучше всего собирать в 5 самых больших по размеру (size) регионах.

SELECT mushrooms.name, mushrooms.description
FROM mushrooms
INNER JOIN regions ON mushrooms.primary_region_id = regions.region_id
WHERE mushrooms.edible = true
ORDER BY regions.size DESC
LIMIT 5

5. Выведите названия всех грибов, которые растут весной, относятся к категории “Пластинчатые” и 
их лучше всего собирать в местах размером до 6000 условных единиц (size).

SELECT mushrooms.name
FROM mushrooms
JOIN categories ON mushrooms.category_id = categories.category_id
JOIN regions ON mushrooms.primary_region_id = regions.region_id
WHERE mushrooms.season = 'spring' 
AND categories.name = 'Пластинчатые'
AND regions.size <= 6000