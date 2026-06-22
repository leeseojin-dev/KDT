import MySQLdb

def get_connection():
    return MySQLdb.connect(
        host='localhost',
        user='root',
        password='1234',
        db='online_store',
        charset='utf8mb4',
    )