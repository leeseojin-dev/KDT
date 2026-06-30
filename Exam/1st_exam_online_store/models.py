# 1. 회원 정보
class Member:
    def __init__(self, member_id, username, password, name, email, regdate):
        self.member_id = member_id
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.regdate = regdate

    @property
    def member_id(self):
        return self.__member_id
    
    @member_id.setter
    def member_id(self, member_id):
        self.__member_id = member_id
    
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if not username:
            raise ValueError("아이디는 비워둘 수 없습니다")
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not password:
            raise ValueError("비밀번호는 비워둘 수 없습니다")
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("이름은 비워둘 수 없습니다")
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not email:
            raise ValueError("이메일 주소는 비워둘 수 없습니다")
        self.__email = email

    @property
    def regdate(self):
        return self.__regdate
    
    @regdate.setter
    def regdate(self, regdate):
        self.__regdate = regdate
    
    def __repr__(self):
        return f"Member(member_id={self.member_id}, username={self.username}, password=***, name={self.name}, email={self.email}, regdate={self.regdate})"

# 2. 상품 정보
class Product:
    def __init__(self, product_id, product_name, price, stock, created_at):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock
        self.created_at = created_at

    @property
    def product_id(self):
        return self.__product_id
    
    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        if not product_name:
            raise ValueError("상품명은 비워둘 수 없습니다")
        self.__product_name = product_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price is None:
            raise ValueError("상품 가격은 비워둘 수 없습니다")
        self.__price = price

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    def __repr__(self):
        return f"Product(product_id={self.product_id}, product_name={self.product_name}, price={self.price}, stock={self.stock}, created_at={self.created_at})"

# 3. 주문 기본 정보
class OrderHeader:
    def __init__(self, order_header_id, member_id, total_price, status, created_at):
        self.order_header_id = order_header_id
        self.member_id = member_id
        self.total_price = total_price
        self.status = status
        self.created_at = created_at

    @property
    def order_header_id(self):
        return self.__order_header_id
    
    @order_header_id.setter
    def order_header_id(self, order_header_id):
        self.__order_header_id = order_header_id

    @property
    def member_id(self):
        return self.__member_id
    
    @member_id.setter
    def member_id(self, member_id):
        self.__member_id = member_id

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price):
        if total_price is None:
            raise ValueError("주문 전체 금액은 비워둘 수 없습니다")
        self.__total_price = total_price
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if not status:
            raise ValueError("주문 상태는 비워둘 수 없습니다")
        self.__status = status

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    def __repr__(self):
        return f"OrderHeader(order_header_id={self.order_header_id}, member_id={self.member_id}, total_price={self.total_price}, status={self.status}, created_at={self.created_at})"

# 4. 주문 상세 (주문 상품 목록)
class OrderItem:
    def __init__(self, order_item_id, order_header_id, product_id, quantity, price):
        self.order_item_id = order_item_id
        self.order_header_id = order_header_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    @property
    def order_item_id(self):
        return self.__order_item_id
    
    @order_item_id.setter
    def order_item_id(self, order_item_id):
        self.__order_item_id = order_item_id

    @property
    def order_header_id(self):
        return self.__order_header_id
    
    @order_header_id.setter
    def order_header_id(self, order_header_id):
        self.__order_header_id = order_header_id

    @property
    def product_id(self):
        return self.__product_id
    
    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity is None:
            raise ValueError("주문한 상품 수량은 비워둘 수 없습니다")
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price is None:
            raise ValueError("주문 당시 상품 가격은 비워둘 수 없습니다")
        self.__price = price

    def __repr__(self):
        return f"OrderItem(order_item_id={self.order_item_id}, order_header_id={self.order_header_id}, product_id={self.product_id}, quantity={self.quantity}, price={self.price})"

# 5. 결제 정보
class Payment:
    def __init__(self, payment_id, order_header_id, method, paid_amount, paid_at):
        self.payment_id = payment_id
        self.order_header_id = order_header_id
        self.method = method
        self.paid_amount = paid_amount
        self.paid_at = paid_at

    @property
    def payment_id(self):
        return self.__payment_id
    
    @payment_id.setter
    def payment_id(self, payment_id):
        self.__payment_id = payment_id

    @property
    def order_header_id(self):
        return self.__order_header_id
    
    @order_header_id.setter
    def order_header_id(self, order_header_id):
        self.__order_header_id = order_header_id

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method):
        if not method:
            raise ValueError("결제 방식은 비워둘 수 없습니다")
        self.__method = method

    @property
    def paid_amount(self):
        return self.__paid_amount

    @paid_amount.setter
    def paid_amount(self, paid_amount):
        if paid_amount is None:
            raise ValueError("실제 결제 금액은 비워둘 수 없습니다")
        self.__paid_amount = paid_amount

    @property
    def paid_at(self):
        return self.__paid_at
    
    @paid_at.setter
    def paid_at(self, paid_at):
        self.__paid_at = paid_at

    def __repr__(self):
        return f"Payment(payment_id={self.payment_id}, order_header_id={self.order_header_id}, method={self.method}, paid_amount={self.paid_amount}, paid_at={self.paid_at})"
    