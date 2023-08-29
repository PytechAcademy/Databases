```sqlite
sqlite3
.open student_records.db

CREATE TABLE students (
   student_id INTEGER PRIMARY KEY,
   first_name TEXT,
   last_name TEXT,
   age INTEGER,
   major TEXT
);

INSERT INTO students (first_name, last_name, age, major)
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

CREATE TABLE courses (
   course_id INTEGER PRIMARY KEY,
   course_name TEXT,
   instructor TEXT,
   credits INTEGER,
   department TEXT
);

INSERT INTO courses (course_name, instructor, credits, department)
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

SELECT * FROM students WHERE age > 20;

UPDATE students SET age = 26 WHERE first_name = 'John';

DELETE FROM students WHERE age < 21;

SELECT * FROM students;
```
