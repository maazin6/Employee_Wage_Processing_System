create database employee;
use employee;

create table empdata(Empid int primary key,
Empname varchar(50) not null,
Designation varchar(50),
Role char(20) not null,
status varchar(25) not null,
password varchar(50) default 'pass',
basic float, allowence float);

insert into empdata(Empid,Empname,Designation,Role,status,basic,allowence) values(1,'a','Admin','A','A',20000,3000),
(2,'b','Manager','M','A',17000,2000),(3,'c','User','U','A',15000,1000),(4,'u','Admin','U','T',20000,3000);

select * from empdata;
desc empdata;

create table salary(Empid int,month varchar(20), year int default 2020,
basic_hours float, normal_overtime float, 
friday_overtime float, holiday_overtime float, salary float,
foreign key(Empid) references empdata(Empid));

insert into salary values(1,'April',2020,240,10,10,10,20000),(1,'May',2020,220,12,7,10,15000),(2,'April',2020,240,10,10,10,20000),
(3,'May',2020,220,12,7,10,15000),(4,'April',2020,240,10,10,10,20000);

select * from salary;
desc salary;

set sql_safe_updates=0;

delete from salary;
delete from empdata;