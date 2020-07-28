Exercise XP
1. update film set language_id = 2 where film_id < 10
2. Done
	1. The address_id is linked to the table “address” so the address_id has to be an address_id that exists in the address table.
3. Done, No
4. 
5. 
	1.  select * from film where description like '%Sumo Wrestler%' and film_id in (select film_id from film_actor where actor_id in(select actor_id from actor where first_name = 'Penelope' and last_name = 'Monroe'))
	2.   SELECT * FROM film WHERE length < 60 AND rating = 'R' AND description like '%Documentary%'; 
	3.  
	4. 
6.  select  * from Action_Movies
	1. CREATE VIEW Action_Movies  AS
	SELECT title, release_year
	FROM film
	where film_id in (select film_id from film_actor where actor_id in (select 	actor_id from actor where first_name = 'Joe' and last_name = 'Swank' )) 	and description like '%Action%' 

