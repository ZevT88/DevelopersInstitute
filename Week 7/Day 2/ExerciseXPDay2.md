## Exercise #1 (ExerciseXP)
1.  Update
	1. update student set first_name = upper(first_name) where last_name = 'Dupont' 
	2. update student set birth_date = 02/11/1998 where last_name = 'Dupont' 
2.  Delete 
	1. delete from student where first_name = 'Lea' and last_name = 'Dupont' 
3.  Count 
	1. select count(*) from student
	2. select count(*)  from student where birth_date > 1/01/2000
4.  Insert/Alter 
	1. ALTER TABLE student ADD math_grade bigint; 
	2. update student set math_grade = 80 where id = 1 
	3. update student set math_grade = 90 where id = 2 or id = 4 
	4. update student set math_grade = 100 where id = 6 
	5. select count(*) from student where math_grade > 83 
	6. insert into student(first_name, last_name, age, math_grade) values('Omer', 'Simpson', 11/12/13, 70 ) 
	7. SELECT first_name, last_name, COUNT(math_grade) AS total_grade FROM student GROUP BY first_name, last_name;
5.  Sum 
	1. select sum(math_grade) from student




## Exercise #2
1.  
	1. select * from items order by price asc 
	2. select * from items where (price) > 80 order by price desc 
	3. select first_name,  last_name from customers order by first_name  limit 3 
	4. 
	5. select last_name from customers order by last_name desc   

2. CREATE TABLE purchases(
 	customerID int, 
 	foreign key (customerid) REFERENCES customers (costumer_id),
	itemID int,
	foreign key (itemID) REFERENCES items (item_id)
); 

3.     
	1.  select * from purchases 
	2.   SELECT purchases.customerid, purchases.itemid
	FROM purchases
	INNER JOIN customers ON purchases.customerID   = customers.customerid 

	3.  SELECT * from purchases where customerid = 4
	4. select * from purchases where itemid in (1,2) 




4. insert into purchases (customerid,itemid) values(3, 4) 
5. delete from purchases where itemid = 4
6.    No 
7. 


	



 




