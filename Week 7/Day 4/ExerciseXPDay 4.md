# ExerciseXP Day 4

## Basic Select Statement
1.   select first_name as firstname, last_name as lastname from employees
2.  select employee_id from employees limit 1
3.  select * from employees order by first_name desc
4.   select first_name, last_name, salary, salary * 15 / 100 as FifteenPercentSalary from employees
5. select employee_id, first_name, last_name, salary  from employees order by salary desc
6.   select SUM(salary) from employees
7.  select MAX(salary), MIN(salary) from employees 
8.   select AVG(salary) as Average_Salary, COUNT(employee_id) as number_employees from employees
9.  select count(*) from employees
10.  
11.  select UPPER(first_name) from employees
12. SELECT SUBSTRING( first_name, 1, 3 ) FROM employees 
13.  select 171*214+625
14.    select (first_name, last_name) as name from employees
15. 
16.  select first_name, last_name, length(first_name) + length(last_name) from employees 
17. select first_name from employees where first_name like '%[0-9]%' 
18. select * from employees limit 10 
19.  select CAST(ROUND(salary/12, 2) AS DECIMAL(10,2)) from employees  



## Restricting and sorting 
1. select first_name, last_name, department_id from employees where salary between 10000 and 15000 
2. select first_name, last_name, department_id from employees where department_id = 30 or department_id = 100 order by department_id desc
3.  
4. select first_name, last_name, hire_date from employees where cast(hire_date as text) like '%1987%'
5.  select first_name from employees where first_name like '%c%' and first_name like '%e%'
6.  select last_name, job_id, salary from employees where salary not in (4500,10000,15000) and job_id not in (select job_id from jobs where job_title = 'Programmer' or job_title = 'Shipping Clerk' )
7.  select last_name from employees where last_name like '______'
8. select last_name from employees where last_name like '__e%'  
9.  
10. 
11. select * from employees where last_name in('Scott', 'Blake', 'Jones', 'Fords', 'King')  









	