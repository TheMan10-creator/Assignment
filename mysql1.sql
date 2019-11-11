create database assign;
use assign;
create table new_table(fname varchar(30),lname varchar(30), address varchar(30), age int);
insert into new_table(fname,lname,address,age)
values('asis','acharya','ktm',20);
desc new_table;
select * from new_table;
drop table new_table;	

alter table new_table modify age varchar(5);
alter table new_table add column degree varchar(30);
alter table new_table add column contact varchar(15);

