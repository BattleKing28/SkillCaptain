SELECT * FROM `Employees` CROSS JOIN `Department`;

SELECT EmployeeName FROM `Employees` INNER JOIN `Department`  ON Employees.DepartmentID = Department.EmployeeID;

SELECT * FROM `Employees` FULL OUTER JOIN `Department`  ON Employees.DepartmentID = Department.EmployeeID;

SELECT * FROM `Employees` INNER JOIN `Department`  ON Employees.DepartmentID = Department.EmployeeID;

SELECT DepartmentName FROM `Department` INNER JOIN `Employees` ON Department.EmployeeID = Employees.DepartmentID;
