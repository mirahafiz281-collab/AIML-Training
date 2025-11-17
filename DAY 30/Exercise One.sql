create database PassportDb
use PassportDb
create table PersonTable
(PersonId int primary key,
FullName nvarchar(100) not null,
DateOfBirth date not null,
Nationality nvarchar(50) not null
)

select * from PersonTable

create table Passport
(PassportId nvarchar(15) primary key,
PersonId int not null unique foreign key references PersonTable,
PassportNumber nvarchar(50) not null unique,
IssueDate date not null,
ExpiryDate date not null
)

insert into PersonTable values (1,'Sarah','1999-12-22','United Kingdom')
select * from PersonTable

insert into PersonTable values 
(2,'Muhammad','1997-01-12','Egypt'),
(3,'Farah','1980-02-02','Malaysia'),
(4,'Ali','1998-03-23','Australia'),
(5,'Zakwan','1993-04-12','Korea'),
(6,'Wani','1993-04-17','Japan'),
(7,'Tira','1990-08-10','Indonesia'),
(8,'Rayyan','1994-11-04','Jordan')
select * from Persontable

insert into Passport 
values ('Pass-1',1,'P5541','2025-12-24','2029-12-25')

insert into Passport values 
('Pass-2',2,'P5542','2025-02-21','2029-12-21'),
('Pass-3',3,'P5543','2025-03-22','2029-12-22'),
('Pass-4',4,'P5544','2025-04-23','2029-12-23'),
('Pass-5',5,'P5545','2025-05-28','2029-12-28'),
('Pass-6',6,'P5546','2025-06-25','2029-12-25'),
('Pass-7',7,'P5547','2025-07-26','2029-12-26'),
('Pass-8',8,'P5548','2025-08-27','2029-12-27')
select * from Passport

select p.PersonId,p.FullName,p.DateOfBirth,p.Nationality,s.PassportId,s.PassportNumber,s.IssueDate,s.ExpiryDate
from PersonTable p,Passport s
where p.PersonId=s.PersonId
