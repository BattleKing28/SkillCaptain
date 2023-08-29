use employees;

CREATE TABLE `Employees` (
   
    `Name` varchar(50)  NOT NULL 
    
);

INSERT INTO Employees VALUES( 'Phil');
INSERT INTO Employees VALUES( 'Jay');

TRUNCATE Employees;

SELECT * FROM `Employees`;

DROP TABLE `Employees`;