from models import *
from study_dao import *
from datetime import datetime

class StudyService:
    def __init__(self):
        self.dao = StudyDAO()

    # 1. 과목 관리
    def add_subject(self):      # 과목 등록
        subject_name = input("과목명을 입력하세요: ")
        if not subject_name.strip():
            print("과목명은 비워둘 수 없습니다.")
            return

        description = input("과목에 대한 설명을 입력하세요: ")
        subject = Subject(subject_name=subject_name, description=description)
        self.dao.insert_subject(subject)
        print(f"[{subject_name}] 과목이 등록되었습니다")

    def show_subjects(self):    # 과목 전체 출력
        subjects = self.dao.select_all_subjects()
        if not subjects:
            print("등록된 과목이 없습니다")
            return
        for subject in subjects:
            print(f"[{subject['subject_id']}] 과목명: {subject['subject_name']}, 설명: {subject['description']}, 등록일: {subject['created_at']}")

    def delete_subject(self):   # 과목 삭제
        subject_id = input("삭제할 과목 번호를 입력하세요: ")
        if not subject_id.isdigit():
            print("번호는 숫자로 입력해야 합니다.")
            return
        subject = self.dao.select_subject_by_id(subject_id)
        if not subject:
            print("존재하지 않는 과목입니다")
            return
        result = self.dao.delete_subject(subject_id)
        if result == 0:
            print("삭제에 실패했습니다")
            return
        print(f"[{subject['subject_name']}] 과목이 삭제되었습니다")

    # 2. 과제 관리
    def add_task(self):     # 과제 등록
        subject_id = input("등록할 과목 번호를 입력하세요: ")
        if not subject_id.isdigit():
            print("번호는 숫자로 입력해야 합니다.")
            return
        subject = self.dao.select_subject_by_id(subject_id)
        if not subject:
            print("존재하지 않는 과목입니다")
            return

        title = input("과제 제목을 입력하세요: ")
        if not title.strip():
            print("과제 제목은 비워둘 수 없습니다.")
            return
        
        content = input("과제 내용을 입력하세요: ")

        priority = input("우선순위를 입력하세요: ")
        if priority not in ['낮음', '보통', '높음']:
            print("낮음/보통/높음 중 하나를 입력하세요")
            return

        status = input("과제 상태를 입력하세요: ")
        if status not in ['대기', '완료']:
            print("대기/완료 중 하나를 입력하세요")
            return

        due_date = input("마감일을 입력하세요(YYYY-MM-DD): ")
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            print("날짜는 YYYY-MM-DD 형식으로 입력해야 합니다.")
            return
        
        task = Task(None, subject_id, title, content, priority, status, due_date, None)
        self.dao.insert_task(task)
        print(f"[{task.title}] 과제가 등록되었습니다")

    def show_tasks(self):       # 과제 전체 출력
        tasks = self.dao.select_all_tasks()
        if not tasks:
            print("등록된 과제가 없습니다")
            return
        for task in tasks:
            print(f"[{task['task_id']}] 과목번호: {task['subject_id']}, 과제 제목: {task['title']}, 과제 내용: {task['content']}, 우선 순위: {task['priority']}, 과제 상태: {task['status']}, 마감일: {task['due_date']}, 등록일: {task['created_at']}")
    
    # def show_tasks_by_condition():

    # def search_tasks()
    
    # def update_task()
        
    # def complete_task()
        
    # def delete_task()
        
    # # 3. 학습 계획 관리
    # def add_plan():

    # def show_plans():

    # def delete_plan():

    # # 4. 학습 기록 관리
    # def add_log():
    
    # def show_logs():

    # def delete_log():

    # # 5. 과제 메모 관리
    # def add_memo():

    # def show_memos()
        
    # def delete_memo()
        
    # # 6. 요약 정보
    # def show_summary()