create database online_store;
use online_store;

-- 1. 회원 정보 테이블
create table member (
	member_id int auto_increment primary key,
    username varchar(50) unique not null,
    password varchar(255) not null,
    name varchar(50) not null,
    email varchar(50) unique not null,
    regdate datetime default now()
);

-- 2. 상품 정보 테이블
create table product (
	product_id int auto_increment primary key,
    product_name varchar(50) not null,
    price int not null,
    stock int not null default 0,
    created_at datetime default now()
);

-- 3. 주문 기본 정보 테이블
create table order_header (
	order_header_id int auto_increment primary key,
    member_id int not null,
    total_price int not null,
    status varchar(30) not null,
    created_at datetime default now(),
    
    foreign key (member_id) references member(member_id)
);

-- 4. 주문 상세 (주문 상품 목록) 테이블
create table order_item (
	order_item_id int auto_increment primary key,
    order_header_id int not null,
    product_id int not null,
    quantity int not null,
    price int not null,
    
    foreign key (order_header_id) references order_header(order_header_id),
    foreign key (product_id) references product(product_id)
);

-- 5. 결제 정보 테이블
create table payment (
	payment_id int auto_increment primary key,
    order_header_id int unique not null,
    method varchar(20) not null,
    paid_amount int not null,
    paid_at datetime default now(),
    
    foreign key (order_header_id) references order_header(order_header_id)
);