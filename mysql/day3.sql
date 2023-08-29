INSERT INTO Employees VALUES(6, 'Jerry', 'jerry@gmail.com', 'HR',' 1990-09-18', 60000.00, true);
INSERT INTO Employees VALUES(7, 'Phil', 'phil@gmail.com', 'IT',' 1992-04-19', 80000.00, true);

UPDATE Employees SET `Salary` = 75000 WHERE `ID`=2;

DELETE FROM Employees WHERE `ID`=1;