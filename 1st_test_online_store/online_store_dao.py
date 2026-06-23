import MySQLdb
from db import get_connection
from models import *

class OnlineStoreDAO:
    # 회원 등록
    def insert_member(self, member):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "insert into member (username, password, name, email) values (%s, %s, %s, %s)"
            data = (member.username, member.password, member.name, member.email)
            cur.execute(sql, data)
            db.commit()
            cur.close()
        except Exception as e:
            print(f"오류 발생: {e}")
            db.rollback()
            raise
        finally:
            db.close()
    
    # 회원 아이디 검색
    def select_member_by_username(self, username):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from member where username = %s"
            cur.execute(sql, (username,))
            row = cur.fetchone()
            cur.close()
            return row
        except Exception as e:
            print(f"오류 발생: {e}")
            raise
        finally:
            db.close()

    # 회원 이메일 검색
    def select_member_by_email(self, email):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from member where email = %s"
            cur.execute(sql, (email,))
            row = cur.fetchone()
            cur.close()
            return row
        except Exception as e:
            print(f"오류 발생: {e}")
            raise
        finally:
            db.close()

    # 상품 전체 검색
    def select_product_all(self):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from product order by product_name"
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
            raise
        finally:
            db.close()
    
    # 상품 키워드 검색
    def select_product_by_keyword(self, keyword):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from product where product_name Like concat('%%', %s, '%%') order by product_name"
            cur.execute(sql, (keyword,))
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
            raise
        finally:
            db.close()

    # 상품 id 검색
    def select_product_by_id(self, product_id):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select * from product where product_id = %s"
            cur.execute(sql, (product_id,))
            row = cur.fetchone()
            cur.close()
            return row
        except Exception as e:
            print(f"오류 발생: {e}")
            raise
        finally:
            db.close()
    
    # 장바구니에서 결제하기 전
    def insert_cart_order(self, member_id, cart_items):
        db = get_connection()
        try:
            cur = db.cursor()
            total_price = sum(item['price'] * item['quantity'] for item in cart_items)

            # 1) order_header 1개 저장 (장바구니 전체 합계로)
            sql_order_header = "insert into order_header (member_id, total_price, status) values (%s, %s, %s)"
            cur.execute(sql_order_header, (member_id, total_price, "ready"))

            # 방금 생성된 order_header_id 조회
            sql_order_header_id = "select order_header_id from order_header where member_id = %s order by order_header_id desc limit 1"
            cur.execute(sql_order_header_id, (member_id,))
            row = cur.fetchone()
            order_header_id = row[0]

            # 2) 장바구니 항목 수만큼 order_item 저장 + 재고 차감
            for item in cart_items:
                sql_order_item = "insert into order_item (order_header_id, product_id, quantity, price) values (%s, %s, %s, %s)"
                cur.execute(sql_order_item, (order_header_id, item['product_id'], item['quantity'], item['price']))

                sql_product = "update product set stock = stock - %s where product_id = %s and stock >= %s"
                result = cur.execute(sql_product, (item['quantity'], item['product_id'], item['quantity']))
                if result == 0:
                    raise ValueError(f"[{item['product_name']}] 재고가 부족합니다")

            # 3) 한 번에 db 반영
            db.commit()
            cur.close()
            return order_header_id, total_price

        except Exception as e:
            db.rollback()
            print(f"주문 처리 중 오류가 발생하여 처음으로 되돌아갑니다: {e}")
            raise
        finally:
            db.close()
    
    # 결제 진행 시
    def insert_payment(self, order_header_id, method, paid_amount):
        db = get_connection()
        try:
            cur = db.cursor()
            sql_payment = "insert into payment (order_header_id, method, paid_amount) values (%s, %s, %s)"
            data = (order_header_id, method, paid_amount)
            cur.execute(sql_payment, data)

            sql_update_status = "update order_header set status = 'paid' where order_header_id = %s"
            cur.execute(sql_update_status, (order_header_id,))

            db.commit()
            cur.close()

        except Exception as e:
            db.rollback()
            print(f"결제 처리 중 오류가 발생하여 처음으로 되돌아갑니다: {e}")
            raise
        finally:
            db.close()

    # 주문 내역 조회
    def select_order_list_by_member(self, member_id):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = "select order_header_id, total_price, status, created_at from order_header where member_id = %s order by order_header_id desc"
            cur.execute(sql, (member_id,))
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
            raise
        finally:
            db.close()

    #====
    def select_order_items(self, order_header_id):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = (
                "select p.product_name, oi.quantity, oi.price "
                "from order_item oi "
                "join product p on p.product_id = oi.product_id "
                "where oi.order_header_id = %s"
            )
            cur.execute(sql, (order_header_id,))
            rows = cur.fetchall()
            cur.close()
            return rows
        except Exception as e:
            print(f"오류 발생: {e}")
            raise
        finally:
            db.close()

    # 주문 하나의 기본 정보 + 결제 여부 조회
    def select_order_header_with_payment(self, order_header_id, member_id):
        db = get_connection()
        try:
            cur = db.cursor(MySQLdb.cursors.DictCursor)
            sql = (
                "select oh.order_header_id, oh.total_price, oh.status, "
                "p.payment_id "
                "from order_header oh "
                "left join payment p on p.order_header_id = oh.order_header_id "
                "where oh.order_header_id = %s and oh.member_id = %s"
            )
            cur.execute(sql, (order_header_id, member_id))
            row = cur.fetchone()
            cur.close()
            return row
        except Exception as e:
            print(f"오류 발생: {e}")
            raise
        finally:
            db.close()