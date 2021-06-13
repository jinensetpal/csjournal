use mysql; -- maradb initialization

create table STOCK(ItemNo int(4), Item varchar(50), DCode int(3), Qty int(3), UnitPrice int(2), StockDate date);
insert into STOCK values(5005, 'Ball pen 0.5', 102, 100, 16, '2010-03-31');
insert into STOCK values(5003, 'Ball pen 0.25', 102, 150, 20, '2010-01-01');
insert into STOCK values(5002, 'Gel Pen Premium', 101, 125, 14, '2010-02-14');
insert into STOCK values(5006, 'Gel Pen Classic', 101, 200, 22, '2009-01-01');
insert into STOCK values(5001, 'Eraser Small', 102, 210, 5, '2009-03-19');
insert into STOCK values(5004, 'Eraser Big', 102, 60, 10, '2009-12-12');
insert into STOCK values(5009, 'Sharpener Classic', 103, 160, 8, '2009-01-23');

create table Dealers(DCode int(3), Dname varchar(50));
insert into Dealers values(101, 'Reliable Stationers');
insert into Dealers values(103, 'Classic Plastics');
insert into Dealers values(102, 'Clear Deals');

select * from STOCK order by Item asc;
select ItemNo, Item from STOCK where UnitPrice > 10;
select * from STOCK where DCode = 102 || Qty > 100;
select Item, max(UnitPrice) from STOCK group by DCode;
update STOCK set Qty = Qty + 50;
select Item from STOCK;
select avg(Qty) from STOCK;
select DCode, count(Qty) from STOCK group by DCode;
