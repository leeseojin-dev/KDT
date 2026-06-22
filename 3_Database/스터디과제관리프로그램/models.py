# Subject
class Subject: 
    def __init__(self, subject_id, subject_name, description=None, created_at=None):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.description = description
        self.created_at = created_at

    @property
    def subject_id(self):
        return self.__subject_id
    
    @subject_id.setter
    def subject_id(self, subject_id):
        self.__subject_id = subject_id
    
    @property
    def subject_name(self):
        return self.__subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        if not subject_name:
            raise ValueError("과목명은 비워둘 수 없습니다")
        self.__subject_name = subject_name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at
    
    def __repr__(self):
        return f"Subject(subject_id={self.subject_id}, subject_name={self.subject_name}, description={self.description}, created_at={self.created_at})"

# Task
class Task: 
    def __init__(self, task_id, subject_id, title, content, priority, status, due_date, created_at):
        self.task_id = task_id
        self.subject_id = subject_id
        self.title = title
        self.content = content
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.created_at = created_at
    
    @property
    def task_id(self):
        return self.__task_id
    
    @task_id.setter
    def task_id(self, task_id):
        self.__task_id = task_id

    @property
    def subject_id(self):
        return self.__subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        self.__subject_id = subject_id

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("과제 제목은 비워둘 수 없습니다")
        self.__title = title

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def priority(self):
        return self.__priority
    
    @priority.setter
    def priority(self, priority):
        if not priority:
            raise ValueError("우선 순위는 비워둘 수 없습니다")
        self.__priority = priority

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        if not status:
            raise ValueError("과제 상태는 비워둘 수 없습니다")
        self.__status = status

    @property
    def due_date(self):
        return self.__due_date
    
    @due_date.setter
    def due_date(self, due_date):
        self.__due_date = due_date

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    def __repr__(self):
        return f"Task(task_id={self.task_id}, subject_id={self.subject_id}, title={self.title}, content={self.content}, priority={self.priority}, status={self.status}, due_date={self.due_date}, created_at={self.created_at})"

# StudyPlan
class StudyPlan: 
    def __init__(self, plan_id, subject_id, plan_title, plan_date, start_time, end_time, memo, created_at):
        self.plan_id = plan_id
        self.subject_id = subject_id
        self.plan_title = plan_title
        self.plan_date = plan_date
        self.start_time = start_time
        self.end_time = end_time
        self.memo = memo
        self.created_at = created_at

    @property
    def plan_id(self):
        return self.__plan_id
    
    @plan_id.setter
    def plan_id(self, plan_id):
        self.__plan_id = plan_id

    @property
    def subject_id(self):
        return self.__subject_id
    
    @subject_id.setter
    def subject_id(self, subject_id):
        self.__subject_id = subject_id

    @property
    def plan_title(self):
        return self.__plan_title
    
    @plan_title.setter
    def plan_title(self, plan_title):
        if not plan_title:
            raise ValueError("계획 제목은 비워둘 수 없습니다")
        self.__plan_title = plan_title

    @property
    def plan_date(self):
        return self.__plan_date
    
    @plan_date.setter
    def plan_date(self, plan_date):
        self.__plan_date = plan_date

    @property
    def start_time(self):
        return self.__start_time
    
    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def end_time(self):
        return self.__end_time
    
    @end_time.setter
    def end_time(self, end_time):
        self.__end_time = end_time

    @property
    def memo(self):
        return self.__memo
    
    @memo.setter
    def memo(self, memo):
        self.__memo = memo

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    def __repr__(self):
        return f"StudyPlan(plan_id={self.plan_id}, subject_id={self.subject_id}, plan_title={self.plan_title}, plan_date={self.plan_date}, start_time={self.start_time}, end_time={self.end_time}, memo={self.memo}, created_at={self.created_at})"

# StudyLog
class StudyLog: 
    def __init__(self, log_id, subject_id, study_date, study_time, content, created_at):
        self.log_id = log_id
        self.subject_id = subject_id
        self.study_date = study_date
        self.study_time = study_time
        self.content = content
        self.created_at = created_at

    @property
    def log_id(self):
        return self.__log_id
    
    @log_id.setter
    def log_id(self, log_id):
        self.__log_id = log_id

    @property
    def subject_id(self):
        return self.__subject_id
    
    @subject_id.setter
    def subject_id(self, subject_id):
        self.__subject_id = subject_id

    @property
    def study_date(self):
        return self.__study_date
    
    @study_date.setter
    def study_date(self, study_date):
        self.__study_date = study_date

    @property
    def study_time(self):
        return self.__study_time
    
    @study_time.setter
    def study_time(self, study_time):
        self.__study_time = study_time

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content):
        if not content:
            raise ValueError("학습 내용은 비워둘 수 없습니다")
        self.__content = content

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    def __repr__(self):
        return f"StudyLog(log_id={self.log_id}, subject_id={self.subject_id}, study_date={self.study_date}, study_time={self.study_time}, content={self.content}, created_at={self.created_at})"

    
# TaskMemo
class TaskMemo: 
    def __init__(self, memo_id, task_id, memo, created_at):
        self.memo_id = memo_id
        self.task_id = task_id
        self.memo = memo
        self.created_at = created_at

    @property
    def memo_id(self):
        return self.__memo_id
    
    @memo_id.setter
    def memo_id(self, memo_id):
        self.__memo_id = memo_id

    @property
    def task_id(self):
        return self.__task_id
    
    @task_id.setter
    def task_id(self, task_id):
        self.__task_id = task_id

    @property
    def memo(self):
        return self.__memo
    
    @memo.setter
    def memo(self, memo):
        if not memo:
            raise ValueError("과제 메모는 비워둘 수 없습니다")
        self.__memo = memo

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    def __repr__(self):
        return f"TaskMemo(memo_id={self.memo_id}, task_id={self.task_id}, memo={self.memo}, created_at={self.created_at})"
