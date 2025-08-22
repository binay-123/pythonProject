CREATE TABLE Students (
    Stu_ID INT PRIMARY KEY,
    Stu_name VARCHAR(100),
    Stu_address VARCHAR(200)
);
INSERT INTO Students (Stu_ID, Stu_name, Stu_address)
VALUES (1, 'Alice', 'New York');
INSERT INTO Students (Stu_ID, Stu_name, Stu_address)
VALUES (2, 'Bob', 'Los Angeles');
SELECT * FROM Users;
SELECT * FROM Students;