create database SalesDb
use SalesDb

create table Products
(ProductID int primary key,
ProductName nvarchar(100),
Category nvarchar(50),
UnitPrice decimal (10,2)
)
delete from Products
 
insert into Products values (1,'Laptop Xiaomi','Electronics',1200)
select * from Products
insert into Products values
(2,'Wireless Keyboard','Electronics',100),
(3,'Wireless Mouse','Electronics',50),
(4,'Table','Furniture',1300),
(5,'PenBox','Stationary',15),
(6,'Chair','Furniture',350),
(7,'Notebook','Stationary',10.50)

select * from Products
create table Sales
(SalesID int primary key identity,
ProductId int foreign key references Products (ProductId),
Region nvarchar(50) check (Region in ('East','West','North','South')),
Quantity int,
SalesDate date,
)
--YY-MM_DD
insert into Sales (ProductId, Region, Quantity, SalesDate) values (1,'East',5,'2024-02-23')
select * from Sales
insert into Sales
(ProductId, Region, Quantity, SalesDate)
values (2,'West',6,'2024-02-23'),
(2,'North',10,'2024-06-23'),
(3,'East',8,'2024-09-23'),
(4,'South',10,'2024-12-23'),
(4,'West',7,'2024-01-23'),
(5,'East',13,'2024-05-23'),
(6,'East',19,'2024-07-23')

select * from Products
select * from Sales

tuncate tables sales
INSERT INTO Sales (ProductID, Region, Quantity, SaleSDate) VALUES
(1, 'East', 5, '2024-01-10'),
(2, 'West', 10, '2024-01-12'),
(3, 'North', 3, '2024-02-05'),
(4, 'South', 8, '2024-02-10'),
(5, 'East', 2, '2024-03-01'),
(1, 'West', 7, '2024-03-15'),
(3, 'North', 4, '2024-04-03'),
(2, 'South', 6, '2024-04-10'),
(5, 'East', 3, '2024-05-02'),
(4, 'West', 9, '2024-05-10')

select * from Sales
 INSERT INTO Sales (ProductID, Region, Quantity, SaleSDate) VALUES
 (6,'East',5,'2024-02-24')
 select * from Sales