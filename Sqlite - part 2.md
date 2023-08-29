### Sqlite - part 2

**sqlite**> SELECT first_name, last_name, major FROM students WHERE age >= 21;
John|Smith|Computer Science
Emily|Johnson|Biology
Sarah|Davis|Chemistry
Olivia|Miller|Psychology
Sophia|Brown|Engineering
Ethan|Martinez|Economics
Liam|Moore|History
**sqlite**> SELECT COUNT(*) FROM students;
10
**sqlite**> SELECT CURRENT_TIMESTAMP;
2023-08-23 18:34:22
**sqlite**> SELECT * FROM students WHERE first_name LIKE 'J%';
1|John|Smith|22|Computer Science
**sqlite**> SELECT * FROM students WHERE first_name LIKE '_ohn';
1|John|Smith|22|Computer Science
sqlite> SELECT * FROM students WHERE age BETWEEN 20 AND 22;
1|John|Smith|22|Computer Science
2|Emily|Johnson|21|Biology
3|Michael|Williams|20|Mathematics
5|David|Lee|20|Physics
6|Olivia|Miller|21|Psychology
7|Sophia|Brown|22|Engineering
9|Ava|Garcia|20|Art
10|Liam|Moore|21|History
**sqlite**> SELECT * FROM students WHERE age > (SELECT AVG(age) FROM students);
1|John|Smith|22|Computer Science
4|Sarah|Davis|23|Chemistry
7|Sophia|Brown|22|Engineering
8|Ethan|Martinez|23|Economics
sqlite> SELECT * FROM students LIMIT 3 OFFSET 2;
3|Michael|Williams|20|Mathematics
4|Sarah|Davis|23|Chemistry
5|David|Lee|20|Physics
**sqlite**> SELECT age, COUNT(age) FROM students GROUP BY age;
20|3
21|3
22|2
23|2
**sqlite**> SELECT first_name, age FROM students ORDER BY age ASC;
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
**sqlite**> SELECT age, COUNT(age) FROM students GROUP BY age HAVING age > 21;
22|2
23|2