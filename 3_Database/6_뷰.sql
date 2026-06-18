/*
	뷰(view)
    - select 문을 저장해둔 가상의 테이블 (자주 사용하는 select 문 결과를 편하게 사용하기 위해)
		create view 뷰이름 as select문
	- view를 사용하는 이유 (1번과 4번이 가장 큰 특징)
		1. 복잡한 SQL을 단순화
        2. 재사용(자주 쓰는 조회 저장)
        3. 가독성(SQL을 보기 쉽게 구성)
        4. 보안(특정 컬럼만 공개)
	- 데이터를 직접 저장하지 않음 (원본 테이블의 select 결과를 보여주는 가상 테이블. 실제 테이블x)
    - member 테이블 데이터를 변경 -> view 결과도 같이 변경
*/
use ai;
-- 뷰 생성
select userid, name, point from member where point >= 100;
create view vip_member as select userid, name, point from member where point >= 100;
-- 뷰 사용
select * from vip_member;
select * from member;
-- 뷰는 select 처럼 사용 가능
select * from vip_member where point >= 150;
-- 예제 : 회원 주소 view(member_address) userid, name, address1 + address2 + address3 as address
create view member_address as
select userid, name, concat(address1, ' ', address2, ' ', address3) as address from member;
select * from member_address;

-- 뷰 수정
create or replace view vip_member as 
select userid, name, point, email from member where point >= 100;
select * from vip_member;
-- 뷰 구조 확인
show create view vip_member;
-- 뷰 목록 확인
SHOW FULL TABLES WHERE Table_type = 'VIEW';

-- join을 사용해 뷰 생성
select * from orders;
select m.userid, m.name, o.product_name, o.price, o.order_date from member m
join orders o on m.idx = o.member_idx;

create view member_order as
select m.userid, m.name, o.product_name, o.price, o.order_date from member m
join orders o on m.idx = o.member_idx;

select * from member_order;










