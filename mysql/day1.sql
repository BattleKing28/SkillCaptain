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

select * from `Employees`;