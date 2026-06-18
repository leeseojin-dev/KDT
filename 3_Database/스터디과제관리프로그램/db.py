import MySQLdb

def get_connection():
    return MySQLdb.connect(
        host='localhost',
        user='root',
        password='1234',
        db='study_manager',
        charset='utf8'
    )