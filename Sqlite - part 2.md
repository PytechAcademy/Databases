```sqlite
### Sqlite - Part 2

SELECT first_name, last_name, major FROM students WHERE age >= 21;
John|Smith|Computer Science
Emily|Johnson|Biology
Sarah|Davis|Chemistry
Olivia|Miller|Psychology
Sophia|Brown|Engineering
Ethan|Martinez|Economics
Liam|Moore|History

SELECT COUNT(*) FROM students;
10

SELECT CURRENT_TIMESTAMP;
2023-08-23 18:34:22

SELECT * FROM students WHERE first_name LIKE 'J%';
1|John|Smith|22|Computer Science

SELECT * FROM students WHERE first_name LIKE '_ohn';
1|John|Smith|22|Computer Science

SELECT * FROM students WHERE age BETWEEN 20 AND 22;
1|John|Smith|22|Computer Science
2|Emily|Johnson|21|Biology
3|Michael|Williams|20|Mathematics
5|David|Lee|20|Physics
6|Olivia|Miller|21|Psychology
7|Sophia|Brown|22|Engineering
9|Ava|Garcia|20|Art
10|Liam|Moore|21|History

SELECT * FROM students WHERE age > (SELECT AVG(age) FROM students);
1|John|Smith|22|Computer Science
4|Sarah|Davis|23|Chemistry
7|Sophia|Brown|22|Engineering
8|Ethan|Martinez|23|Economics

SELECT * FROM students LIMIT 3 OFFSET 2;
3|Michael|Williams|20|Mathematics
4|Sarah|Davis|23|Chemistry
5|David|Lee|20|Physics

SELECT age, COUNT(age) FROM students GROUP BY age;
20|3
21|3
22|2
23|2

SELECT first_name, age FROM students ORDER BY age ASC;
Michael|20
David|20
Ava|20
Emily|21
Olivia|21
Liam|21
John|22
Sophia|22
Sarah|23
Ethan|23

SELECT age, COUNT(age) FROM students GROUP BY age HAVING age > 21;
22|2
23|2
```
