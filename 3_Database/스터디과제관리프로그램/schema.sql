create database study_manager;

use study_manager;

-- 과목 테이블
create table subjects(
	subject_id int not null primary key,
    subject_name varchar(50) not null,
    description varchar(200),
    created_at datetime default now()
);

-- 과제 테이블
create table tasks(
	task_id int not null primary key, 
    subject_id int not null,
    title varchar(100) not null,
    content text not null,
    priority varchar(10),
    status varchar(10),
    due_date date,
    created_at datetime default now()
);
