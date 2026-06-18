use ai;
show databases;
show tables;

select * from member;

-- root 계정이 아닌 다른 계정에서는 create user가 불가능
create user 'banana'@'localhost' identified by '2222';