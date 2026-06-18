/*
	사용자 계정
    - 데이터베이스에 접속할 수 있는 로그인 계정
    - root 계정은 모든 권한을 가진 계정이기 때문에 실제 사용시 위험할 수 있음
    - 프로젝트 별로 게정을 따로 만들고, 필요한 권한만 부여하는 것이 일반적
*/
-- create user '계정명'@'접속위치' identified by '비밀번호';
-- localhost : 같은 컴퓨터(내 컴퓨텅)에서만 접속
-- 'apple'@'%' : 어디서든 접속 가능
-- 'apple'@'192.168.0.%' : 192.168.0.으로 시작하는 내부망에서만 접속이 가능
-- 'apple'@'192.168.0.10' : 특정 ip에서만 접속 가능
create user 'apple'@'localhost' identified by '1111';

-- <slack의 ip 내용>
-- cmd에서 ipconfig로 ip주소 확인가능
-- 강의실 내의 컴퓨터의 ip주소는 192.168.9.- 로 같은 공유기를 사용중이라서 가상 ip주소이다
-- 네이버에서 내 ip 검색 시 강의실 내의 컴퓨터의 ip주소가 모두 123.142.55.115인 것을 알 수 있다.
-- (실제 학원으로 들어오는 ip는 일정할 것이고 공유기를 통해 여러 컴퓨터들을 연결하여 인터넷을 사용하는 ip 주소)

-- grant 권한종류 on 데이터베이스명.테이블명 to '계정명'@'접속위치';
-- all : 모든 일반 권한. select, insert, update, delete, create, drop, alter, index
-- ai.* : ai 데이터베이스 안의 모든 테이블 (*.*, ai.member)
grant all on ai.* to 'apple'@'localhost';
-- show로 권한 확인하기
show grants for 'apple'@'localhost';
-- 김사과 계정으로 로그인해보고 파일 만들어보기

-- 새로운 바나나 계정 생성 후 select 권한만 주기
create user 'banana'@'localhost' identified by '2222';
grant select on ai.* to 'banana'@'localhost';
-- 반하나 계정으로 로그인해보고 파일 만들어보기

-- 새로운 오렌지 계정 생성 후 select, insert, update, delete 권한 주기
create user 'orange'@'localhost' identified by '3333';
grant select, insert, update, delete on ai.* to 'orange'@'localhost';
-- 오렌지 게정으로 로그인해보고 파일 만들어보기

-- 권환 회수하기
revoke delete on ai.* from 'orange'@'localhost';

-- 사용자 비밀번호 변경
alter user 'banana'@'localhost' identified by '1004';

-- 사용자 삭제
drop user 'banana'@'localhost';

-- 예제 : 다른 컴퓨터에서 접속하기
-- 1. 데이터베이스 생성 : testdb
create database testdb;
show databases;
use testdb;
-- 2. 테이블 생성 : test_member 스키마 가져와서
create table member (
	idx int auto_increment primary key,
    userid varchar(20) unique not null,
    userpw varchar(20) not null,
    name varchar(20) not null,
    hp varchar(20) not null,
    email varchar(50) not null,
    ssn1 char(6) not null,
    ssn2 char(7) not null,
    zipcode varchar(5),
    address1 varchar(100),
    address2 varchar(100),
    address3 varchar(100),
    regdate datetime default now(),
    point int default 100
);
-- 3. 사용자 게정 생성 : user1/1111, user2/1111. 권한 select, update, insert만
create user 'user1'@'192.168.12.172' identified by '1111';
create user 'user2'@'192.168.%' identified by '1111';
grant select, update, insert on testdb.* to 'user1'@'192.168.12.172';
grant select, update, insert on testdb.* to 'user2'@'192.168.%';

select * from member;



