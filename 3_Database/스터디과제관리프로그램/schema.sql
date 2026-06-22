create database study_manager;

use study_manager;

-- 과목 테이블
create table subjects(
	subject_id int auto_increment primary key,
    subject_name varchar(50) not null,
    description varchar(200),
    created_at datetime default now()
);

-- 과제 테이블
create table tasks(
    task_id int auto_increment primary key, 
    subject_id int not null,
    title varchar(100) not null,
    content text,
    priority varchar(10) not null,
    status varchar(10) not null,
    due_date date,
    created_at datetime default now(),
    
    foreign key (subject_id) references subjects(subject_id)
);

-- 스터디 플랜 테이블
create table study_plans(
	plan_id int auto_increment primary key,
    subject_id int not null,
    plan_title varchar(100) not null,
    plan_date date,
    start_time time,
    end_time time,
    memo varchar(200),
    created_at datetime default now(),
    
    foreign key (subject_id) references subjects(subject_id)
);

-- 스터디 로그 테이블
create table study_logs(
	log_id int auto_increment primary key,
    subject_id int not null,
    study_date date,
    study_time int,
    content varchar(300) not null,
    created_at datetime default now(),
    
	foreign key (subject_id) references subjects(subject_id)
);

-- 과제 메모 테이블
create table task_memos(
	memo_id int auto_increment primary key,
    task_id int not null,
    memo varchar(300) not null,
    created_at datetime default now(),
    
    foreign key (task_id) references tasks(task_id)
);

-- drop database study_manager; 
