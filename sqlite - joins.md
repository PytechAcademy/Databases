```sqlite
sqlite> .open company.db

sqlite> CREATE TABLE employees (
   emp_id INTEGER PRIMARY KEY,
   emp_name TEXT,
   department TEXT
);

sqlite> INSERT INTO employees (emp_name, department) VALUES
   ('John', 'IT'),
   ('Emily', 'HR'),
   ('Michael', 'IT'),
   ('Sarah', 'Marketing');

sqlite> CREATE TABLE projects (
   project_id INTEGER PRIMARY KEY,
   project_name TEXT,
   assigned_emp_id INTEGER
);

sqlite> INSERT INTO projects (project_name, assigned_emp_id) VALUES
   ('Website Redesign', 1),
   ('HR Training', 2),
   ('App Development', NULL),
   ('Campaign Launch', 4);

sqlite> SELECT employees.emp_name, projects.project_name
   FROM employees
   INNER JOIN projects ON employees.emp_id = projects.assigned_emp_id;
John|Website Redesign
Emily|HR Training
Sarah|Campaign Launch

sqlite> SELECT employees.emp_name, projects.project_name
   FROM employees
   LEFT JOIN projects ON employees.emp_id = projects.assigned_emp_id;
John|Website Redesign
Emily|HR Training
Michael|
Sarah|Campaign Launch

sqlite> SELECT employees.emp_name, projects.project_name
   FROM employees
   RIGHT JOIN projects ON employees.emp_id = projects.assigned_emp_id;
John|Website Redesign
Emily|HR Training
Sarah|Campaign Launch
|App Development

sqlite> SELECT employees.emp_name, projects.project_name
   FROM employees
   FULL JOIN projects ON employees.emp_id = projects.assigned_emp_id;
John|Website Redesign
Emily|HR Training
Michael|
Sarah|Campaign Launch
|App Development
```
