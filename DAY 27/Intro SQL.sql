--create object objectName

create database OurDb
-- create table <TableName>
--(ColumnName DataType <constratint>,
------------
---)
use OurDb
create table Student
(SId int primary key,
SName nvarchar(50) not null,
SFee float not null)
----------------------
select * from Student
insert into Student values (1,'Sam',5000.50)
insert into Student values
(2, 'Rohit',4500.58),
(3,'Neha',5000.45),
(4,'Ali',4800.45),
(5,'Fara',5500.45)
select * from Student