-- Query: Create 3 ninjas that belong to the first dojo
insert into ninjas (first_name , last_name , age, dojo_id) values ('samah' , 'nasri' , 28 , '4');
insert into ninjas (first_name , last_name , age, dojo_id) values ('imen' , 'ncir' , 30 , '4');
insert into ninjas (first_name , last_name , age, dojo_id) values ('samira' , 'chohaoui' , 28 , '4');
select * from ninjas;

-- Query: Create 3 ninjas that belong to the second dojo
insert into ninjas (first_name , last_name , age, dojo_id) values ('mogded' , 'nasri' , 36 , '5' );
insert into ninjas (first_name , last_name , age, dojo_id) values ('dali' , 'nasri' , 33 , '5' );
insert into ninjas (first_name , last_name , age, dojo_id) values ('salwa' , 'nasri' , 45 , '5' );

-- Query: Create 3 ninjas that belong to the third dojo
insert into ninjas (first_name , last_name , age, dojo_id) values ('yakin' , 'fathallah' , 8 , '6' );
insert into ninjas (first_name , last_name , age, dojo_id) values ('amine' , 'fathallah' , 10 , '6' );
insert into ninjas (first_name , last_name , age, dojo_id) values ('tahar' , 'fathallah' , 52 , '6' );

-- Query: Retrieve all the ninjas from the first dojo
SELECT *
 FROM ninjas
 JOIN dojos
 ON ninjas.dojo_id = dojos.id
 WHERE ninjas.dojo_id = '4';

-- Query: Retrieve all the ninjas from the last dojo
SELECT *
FROM ninjas
JOIN dojos
ON ninjas.dojo_id = dojos.id
WHERE ninjas.dojo_id = '6';

-- Query: Retrieve the last ninja's dojo
 SELECT *
 FROM ninjas
 JOIN dojos
 ON ninjas.dojo_id = dojos.id
 WHERE ninjas.id = '9';