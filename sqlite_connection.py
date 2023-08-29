import sqlite3
# Connect to a database or create a new one if it doesn't exist
conn = sqlite3.connect('databasename.db')
# Create a table named 'COMPANY'
conn.execute('''CREATE TABLE COMPANY (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
);''')
# Insert data into the 'COMPANY' table
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (1, 'John', 25, '123 Main St', 50000.0)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (2, 'Jane', 30, '456 Elm St', 60000.0)")
# Commit the changes
conn.commit()
# Retrieve all rows from the 'COMPANY' table
result = conn.execute("SELECT * FROM COMPANY")
for row in result:
    print(row)
# Update the salary for a specific employee
conn.execute("UPDATE COMPANY SET SALARY = 55000.0 WHERE ID = 1")
conn.commit()
# Delete a specific employee from the 'COMPANY' table
conn.execute("DELETE FROM COMPANY WHERE ID = 2")
conn.commit()