use ai;

select * from member;

-- banana 계정은 select 권한만 있기 때문에 에러 발생
-- insert 권한 없음
insert into member (userid, userpw, name, hp, email, ssn1, ssn2, zipcode, address1, address2, address3, gender) values ('test', '1111', '테스트', '010-1111-1111', 'apple@apple.com', '001011', '4011111', '12345', '서울 서초구', '양재동', '111-11', '여자');
