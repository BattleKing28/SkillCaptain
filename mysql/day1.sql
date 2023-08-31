CREATE TABLE `Employees` (
    `ID` int  NOT NULL ,
    `Name` varchar(50)  NOT NULL ,
    `EmailAddress` varchar(50)  NOT NULL ,
    `Department` varchar(50)  NOT NULL ,
    `DateOfBirth` Date  NOT NULL ,
    `Salary` Decimal  NOT NULL ,
    `IsActive` Boolean  NOT NULL 
);
INSERT INTO Employees VALUES(1, 'Mark', 'mark@gmail.com', 'IT',' 2000-05-28', 50000.00, true);
INSERT INTO Employees VALUES(2, 'John', 'john@gmail.com', 'HR',' 1995-05-28', 10000.00, true);
INSERT INTO Employees VALUES(7, 'Ellie', 'ellie@gmail.com', 'HR',' 1995-05-28', 100000.00, true);
INSERT INTO Employees VALUES(8, 'Tess', 'tess@gmail.com', 'IT',' 1995-05-28', 200000.00, true);
INSERT INTO Employees VALUES(3, 'Jay', 'jay@gmail.com', 'Intern',' 2005-06-08', 4000.00, true);
INSERT INTO Employees VALUES(4, 'James', 'james@gmail.com', 'Legal',' 2000-09-18', 34000.00, true);
INSERT INTO Employees VALUES(5, 'Ethan', 'ethan@gmail.com', 'IT',' 1999-04-02', 24000.00, true);
INSERT INTO Employees VALUES(6, 'Joe', 'joe@gmail.com', 'IT',' 1999-04-02', 240000.00, true);

