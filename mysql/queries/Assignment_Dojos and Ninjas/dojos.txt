-- Query: Create 3 new dojos
insert into dojos (name) values ('x');
insert into dojos (name) values ('y');
insert into dojos (name) values ('z');
select * from dojos;

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id IN (1, 2, 3);

-- Query: Create 3 more dojos
insert into dojos (name) values ('q');
insert into dojos (name) values ('w');
insert into dojos (name) values ('r');





