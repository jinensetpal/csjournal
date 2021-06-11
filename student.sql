create table STUDENT(No int(3), Name varchar(50), Stipend float(5,2), Stream varchar(20), AvgMark float(3,1), Grade char(1), Class char(3));

insert into STUDENT values('1.', 'Karan', 400.00, 'Medical', 78.5, 'B', '12B');
insert into STUDENT values('2.', 'Mohit', 450.00, 'Comm.', 89.2, 'A', '11C');
insert into STUDENT values('3.', 'Divya', 300.00, 'Comm.', 68.6, 'C', '12C');
insert into STUDENT values('4.', 'Arun', 350.00, 'Arts', 73.1, 'B', '12D');
insert into STUDENT values('5.', 'John', 500.00, 'NMed', 90.6, 'A', '11A');
insert into STUDENT values('6.', 'Mohan', 400.00, 'Medical', 75.4, 'B', '12B');
insert into STUDENT values('7.', 'Vikas', 250.00, 'Arts', 64.4, 'C', '11A');
insert into STUDENT values('8.', 'Akash', 450.00, 'NMed', 88.5, 'A', '12A');
insert into STUDENT values('9.', 'Bobby', 500.00, 'NMed', 92.0, 'A', '12A');
insert into STUDENT values('10.', 'Abha', 300.00, 'Comm.', 67.5, 'C', '12C');

select distinct(Stream) from STUDENT;
select Name from STUDENT order by Stipend where Class = '12_';
select * from STUDENT order by AvgMark desc;
select Name, Stipend, Stream, Stipend * 12 as Amount from STUDENT;
select sum(Grade) from STUDENT where Grade = 'A';
select sum(Name) from STUDENT group by class;
select sum(Grade) from STUDENT group by Stream where Grade = 'C';
