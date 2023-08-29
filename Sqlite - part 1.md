**sqlite**> .open student_records.db

**sqlite**> CREATE TABLE students (
       student_id INTEGER PRIMARY KEY,
       first_name TEXT,
       last_name TEXT,
       age INTEGER,
       major TEXT
   );
   
**sqlite**> INSERT INTO students (first_name, last_name, age, major)
   VALUES ('John', 'Smith', 22, 'Computer Science'),
          ('Emily', 'Johnson', 21, 'Biology'),
          ('Michael', 'Williams', 20, 'Mathematics'),
          ('Sarah', 'Davis', 23, 'Chemistry'),
          ('David', 'Lee', 20, 'Physics'),
          ('Olivia', 'Miller', 21, 'Psychology'),
          ('Sophia', 'Brown', 22, 'Engineering'),
          ('Ethan', 'Martinez', 23, 'Economics'),
          ('Ava', 'Garcia', 20, 'Art'),
          ('Liam', 'Moore', 21, 'History');
          
**sqlite**> CREATE TABLE courses (
       course_id INTEGER PRIMARY KEY,
       course_name TEXT,
       instructor TEXT,
       credits INTEGER,
       department TEXT
   );
   
**sqlite**> INSERT INTO courses (course_name, instructor, credits, department)
   VALUES ('Database Systems', 'Prof. Anderson', 3, 'Computer Science'),
          ('Biology 101', 'Prof. Martinez', 4, 'Biology'),
          ('Calculus I', 'Prof. Davis', 4, 'Mathematics'),
          ('Chemistry Basics', 'Prof. Smith', 3, 'Chemistry'),
          ('Modern Physics', 'Prof. Miller', 4, 'Physics'),
          ('Psychology 101', 'Prof. Taylor', 3, 'Psychology'),
          ('Introduction to Engineering', 'Prof. Johnson', 3, 'Engineering'),
          ('Microeconomics', 'Prof. Brown', 3, 'Economics'),
          ('Art History', 'Prof. Garcia', 4, 'Art'),
          ('World History', 'Prof. Moore', 4, 'History');
          
**sqlite**> SELECT * FROM students WHERE age > 20;
1|John|Smith|22|Computer Science
2|Emily|Johnson|21|Biology
4|Sarah|Davis|23|Chemistry
6|Olivia|Miller|21|Psychology
7|Sophia|Brown|22|Engineering
8|Ethan|Martinez|23|Economics
10|Liam|Moore|21|History

**sqlite**> UPDATE students SET age = 26 WHERE first_name = 'John';

**sqlite**> DELETE FROM students WHERE age <21;

**sqlite**> SELECT * FROM students;

1|John|Smith|26|Computer Science
2|Emily|Johnson|21|Biology
4|Sarah|Davis|23|Chemistry
6|Olivia|Miller|21|Psychology
7|Sophia|Brown|22|Engineering
8|Ethan|Martinez|23|Economics
10|Liam|Moore|21|History
