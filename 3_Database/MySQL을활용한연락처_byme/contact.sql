use ai;
show databases;

create table contact(
	id int auto_increment primary key,
	name varchar(50) not null,
    phone char(13) not null,
    memo varchar(50)
);

select * from contact;

insert into contact (name, phone) values ('김사과', '010-1111-1111');
insert into contact (name, phone) values ('반하나', '010-2222-2222');
insert into contact (name, phone) values ('오렌지', '010-3333-3333');