-- Active: 1693230356382@@127.0.0.1@3306@test

SELECT * FROM `Employees`;


SELECT `Department`, COUNT(`Name`) FROM `Employees`  GROUP BY `Department`  HAVING COUNT(`Name`) > 2 ORDER BY COUNT(`Name`) DESC;

