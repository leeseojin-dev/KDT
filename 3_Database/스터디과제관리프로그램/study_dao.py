import MySQLdb
from db import get_connection
from models import *

class StudyDAO:
    # 과목
    def insert_subject(self, subject):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "insert into subjects (subject_name, description) values (%s, %s)"
            data = (subject.subject_name, subject.description)
            cur.execute(sql, data)
            db.commit()
            cur.close()
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    def select_all_subjects(self):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from subjects"
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows            
        except Exception as e:
            print(f"오류 발생: {e}")
        finally:
            db.close()

    def delete_subject(self, subject_id):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "delete from subjects where subject_id = %s"
            result = cur.execute(sql, (subject_id,))
            db.commit()
            cur.close()
            return result

        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    # 과제
    def insert_task(self, task):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "insert into tasks (subject_id, title, content, priority, status, due_date) values (%s, %s, %s, %s, %s, %s)"
            data = (task.subject_id, task.title, task.content, task.priority, task.status, task.due_date)
            cur.execute(sql, data)
            db.commit()
            cur.close()
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    def select_all_tasks(self):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from tasks"
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows            
        except Exception as e:
            print(f"오류 발생: {e}")
        finally:
            db.close()

    def select_tasks_by_condition(self, task):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from tasks where subject_id = %s AND priority = %s AND status = %s"
            data = (task.subject_id, task.priority, task.status)
            cur.execute(sql, data)
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
        finally:
            db.close()

    def search_tasks(self, keyword):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from tasks where title like concat('%%', %s, '%%') OR content Like concat('%%', %s, '%%')"
            data = (keyword, keyword)
            cur.execute(sql, data)
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
        finally:
            db.close()

    def update_task(self, task):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "update tasks set title = %s, content = %s, priority = %s, due_date = %s where task_id = %s"
            data = (task.title, task.content, task.priority, task.due_date, task.task_id)
            result = cur.execute(sql, data)
            db.commit()
            cur.close()
            return result
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    def complete_task(self, task_id):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "update tasks set status = '완료' where task_id = %s"
            result = cur.execute(sql, (task_id,))
            db.commit()
            cur.close()
            return result
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    def delete_task(self, task_id):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "delete from tasks where task_id = %s"
            result = cur.execute(sql, (task_id,))
            db.commit()
            cur.close()
            return result
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    # 학습 계획 관리
    def insert_plan(self, studyplan):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "insert into study_plans (subject_id, plan_title, plan_date, start_time, end_time, memo) values (%s, %s, %s, %s, %s, %s)"
            data = (studyplan.subject_id, studyplan.plan_title, studyplan.plan_date, studyplan.start_time, studyplan.end_time, studyplan.memo)
            cur.execute(sql, data)
            db.commit()
            cur.close()
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    def select_all_plans(self):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from study_plans"
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
        finally:
            db.close()

    def delete_plan(self, plan_id):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "delete from study_plans where plan_id = %s"
            result = cur.execute(sql, (plan_id,))
            db.commit()
            cur.close()
            return result
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    # 학습 기록 관리
    def insert_log(self, studylog):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "insert into study_logs (subject_id, study_date, study_time, content) values (%s, %s, %s, %s)"
            data = (studylog.subject_id, studylog.study_date, studylog.study_time, studylog.content)
            cur.execute(sql, data)
            db.commit()
            cur.close()
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    def select_all_logs(self):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from study_logs"
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
        finally:
            db.close()

    def delete_log(self, log_id):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "delete from study_logs where log_id = %s"
            result = cur.execute(sql, (log_id,))
            db.commit()
            cur.close()
            return result
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()

    # 메모
    def insert_memo(self, taskmemo):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "insert into task_memos (task_id, memo) values (%s, %s)"
            data = (taskmemo.task_id, taskmemo.memo)
            cur.execute(sql, data)
            db.commit()
            cur.close()
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()
        
    def select_all_memos(self, task_id=None):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            if task_id:
                sql = "select * from task_memos where task_id = %s"
                cur.execute(sql, (task_id,))
            else:
                sql = "select * from task_memos"
                cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
        finally:
            db.close()
        
    def delete_memo(self, memo_id):
        db = get_connection()
        try:
            cur = db.cursor()
            sql = "delete from task_memos where memo_id = %s"
            result = cur.execute(sql, (memo_id,))
            db.commit()
            cur.close()
            return result
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
        finally:
            db.close()