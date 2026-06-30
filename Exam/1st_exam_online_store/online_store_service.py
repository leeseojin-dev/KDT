from models import *
from online_store_dao import OnlineStoreDAO

class OnlineStoreService:
    def __init__(self):
        self.dao = OnlineStoreDAO()
        self.current_user = None   # 로그인한 회원 정보 저장
        self.cart = []      # 장바구니

    # 1. 회원가입 기능
    def signup(self):
        username = input("아이디를 입력하세요: ")
        if not username.strip():
            print("아이디는 비워둘 수 없습니다")
            return
        
        # 아이디 중복 체크
        if self.dao.select_member_by_username(username) is not None:
            print("이미 사용 중인 아이디입니다")
            return
        
        password = input("비밀번호를 입력하세요: ")
        if not password.strip():
            print("비밀번호는 비워둘 수 없습니다")
            return
        
        name = input("이름(실명)을 입력하세요: ")
        if not name.strip():
            print("이름(실명)은 비워둘 수 없습니다")
            return
        
        email = input("이메일을 입력하세요: ")
        if not email.strip():
            print("이메일은 비워둘 수 없습니다")
            return
        
        # 이메일 중복 체크
        if self.dao.select_member_by_email(email) is not None:
            print("이미 사용 중인 이메일입니다")
            return
        
        member = Member(None, username, password, name, email, None)
        try:
            self.dao.insert_member(member)
        except Exception:
            print("회원가입 중 오류가 발생했습니다. 다시 시도해주세요.")
            return

        print(f"[{username}]님 회원가입이 [완료]되었습니다")

    # 2. 로그인 기능
    def login(self):
        username = input("아이디를 입력하세요: ")
        if not username.strip():
            print("!!!!!아이디를 입력하세요!!!!!: ")
            return
        
        password = input("비밀번호를 입력하세요: ")
        if not password.strip():
            print("!!!!!비밀번호를 입력하세요!!!!!: ")
            return
        
        member = self.dao.select_member_by_username(username)
        if member is None:
            print("아이디가 존재하지 않습니다")
            return

        if member["password"] != password:
            print("비밀번호가 일치하지 않습니다")
            return
        
        self.current_user = member
        print(f"[{member['username']}]님, 로그인 되었습니다")

    # 3. 로그아웃 기능
    def logout(self):
        self.current_user = None
        print("로그아웃 되었습니다")
        return
    
    # 4. 상품 목록 조회 기능
    def show_product(self):
        products = self.dao.select_product_all()
        if not products:
            print("상품 목록이 존재하지 않습니다")
            return
        print(f"|{'ID':<5}|{'상품명':<15}|{'가격':<12}|{'재고':<8}|")
        print("=" * 56)
        for product in products:
            stock_display = "품절" if product['stock'] == 0 else str(product['stock'])
            price_display = f"{product['price']:,}원"
            name = product['product_name']
            name_display = name + " " * max(16 - sum(2 if ord(c) > 127 else 1 for c in name), 0)
            print(f"|{product['product_id']:<5}|{name_display}|{price_display:<12}|{stock_display:<8}|")

    # 5. 상품 검색 기능
    def search_product(self):
        keyword = input("검색어를 입력하세요: ")
        if not keyword.strip():
            print("!!!!!검색어를 입력해주세요!!!!!: ")
            return

        products = self.dao.select_product_by_keyword(keyword)
        if not products:
            print("검색 결과 없음")
            return
        for product in products:
            stock_display = "품절" if product['stock'] == 0 else product['stock']     
            print(f"[상품 ID: {product['product_id']}] 상품명: {product['product_name']} | 상품 가격: {product['price']} | 재고 수량: {stock_display}")

    # 6. 주문 생성 기능
    def order_product(self):
        if self.cart:
            while True:
                yn = input("장바구니에 담긴 상품을 결제하시겠습니까?(y/n): ")
                if yn in ('y', 'n'):
                    break
                print("y 또는 n을 입력하세요")

            if yn == 'y':
                self.checkout_cart()   # 결제 화면으로 이동
                return
            
        # 상품 존재 여부 확인
        product_id = input("주문할 상품 ID를 입력하세요: ")
        if not product_id.strip().isdigit():
            print("올바른 상품 ID를 입력해주세요")
            return
        product = self.dao.select_product_by_id(int(product_id))
        if product is None:
            print("존재하지 않는 상품입니다")
            return
        
        # 상품 수량 확인
        quantity = input("주문할 상품의 수량을 입력하세요: ")
        if not quantity.strip().isdigit() or int(quantity) <= 0:
            print("1개 이상 주문이 가능합니다. 주문할 상품의 수량을 입력하세요: ")
            return
        quantity = int(quantity)

        if product['stock'] < quantity:
            print(f"상품 재고가 부족합니다 (현재 재고: {product['stock']}개)")
            return
        
        # 주문할 상품의 총 금액
        total_price = product['price'] * quantity

        print("\n======= 주문 확인 =======")
        print(f"상품명 : {product['product_name']}")
        print(f"수량   : {quantity}")
        print(f"총 금액: {total_price:,}원")
        print("==========================")
            
        # 주문 생성 여부 확인
        while True:
            yn = input("장바구니에 담으시겠습니까?(y/n): ")
            if yn in ('y', 'n'):
                break
            print("y 또는 n을 입력하세요")

        if yn == 'n':
            print("주문이 [취소]되었습니다. 메인 메뉴로 이동합니다")
            return
        
        # 장바구니
        for item in self.cart:
            if item['product_id'] == product['product_id']:
                item['quantity'] += quantity
                print(f"\n[{product['product_name']}] 장바구니 수량이 {item['quantity']}개로 변경되었습니다")
                return

        self.cart.append({
            "product_id": product['product_id'],
            "product_name": product['product_name'],
            "price": product['price'],
            "quantity": quantity,
        })
        print(f"\n[{product['product_name']}] {quantity}개가 장바구니에 담겼습니다")
    
    # 장바구니 확인
    def checkout_cart(self):
        if not self.cart:
            print("장바구니가 비어있습니다")
            return

        print("\n======= 장바구니 =======")
        for item in self.cart:
            line_total = item['price'] * item['quantity']
            print(f"{item['product_name']} | 수량: {item['quantity']} | 금액: {line_total:,}원")
        total_price = sum(item['price'] * item['quantity'] for item in self.cart)
        print(f"------------------------")
        print(f"총 금액: {total_price:,}원")
        print("=========================")

        while True:
            yn = input("주문을 진행하시겠습니까?(y/n): ")
            if yn in ('y', 'n'):
                break
            print("y 또는 n을 입력하세요")

        if yn == 'n':
            print("주문이 [취소]되었습니다. 메인 메뉴로 이동합니다")
            return

        try:
            order_header_id, total_price = self.dao.insert_cart_order(member_id=self.current_user['member_id'], cart_items=self.cart)
        except Exception:
            print("주문 처리 중 오류가 발생했습니다. 다시 시도해주세요.")
            return
        print(f"\n주문 생성이 [완료]되었습니다. (주문번호: {order_header_id})")

        # 장바구니 비우기
        self.cart = []

        # 결제로 이어서 진행 (기존 pay() 그대로 재사용)
        self.pay(order_header_id, total_price)

    # 7. 결제 기능
    def pay(self, order_header_id, total_price):
        print("======== 결제 방식 ========")
        print("1. 카드")
        print("2. 계좌이체")
        print("==========================")

        while True:
            choice_payment_method = input("결제 방식을 선택하세요(1 또는 2): ")
            if choice_payment_method not in ('1', '2'):
                print("1 또는 2를 입력하세요")
            else:
                break
        
        while True:
            yn = input("결제를 진행하시겠습니까?(y/n): ")
            if yn in ('y', 'n'):
                break
            print("y 또는 n을 입력하세요")

        if yn == 'n':
            print("결제가 [취소]되었습니다. 메인 메뉴로 이동합니다")
            return
        
        method = "card" if choice_payment_method == '1' else "bank"
        paid_amount = total_price

        try:
            self.dao.insert_payment(order_header_id, method, paid_amount)
        except Exception:
            print("결제 처리 중 오류가 발생했습니다. 다시 시도해주세요.")
            return

        print("결제가 [완료]되었습니다. 메인 메뉴로 이동합니다")

    # 8. 주문 내역 조회 기능
    def show_order_list(self):
        orders = self.dao.select_order_list_by_member(self.current_user['member_id'])
        if not orders:
            print("주문 내역이 존재하지 않습니다")
            return

        print(f"|{'주문번호':<10}|{'총금액':<14}|{'상태':<10}|{'주문일자':<20}|")
        print("=" * 54)
        for order in orders:
            price_str = f"{order['total_price']:,}원"
            print(f"|{order['order_header_id']:<10}|{price_str:<14}|{order['status']:<10}|{str(order['created_at']):<20}|")

        order_id_input = input("\n상세 조회할 주문번호를 입력하세요 (0: 돌아가기): ")
        if not order_id_input.strip().isdigit():
            print("올바른 주문번호를 입력해주세요")
            return
        order_id_input = int(order_id_input)

        if order_id_input == 0:
            return

        self.show_order_detail(order_id_input)

    # 주문 상세 정보 출력
    def show_order_detail(self, order_header_id):
        header = self.dao.select_order_header_with_payment(order_header_id, self.current_user['member_id'])
        if header is None:
            print("존재하지 않는 주문이거나 본인의 주문이 아닙니다")
            return

        items = self.dao.select_order_items(order_header_id)

        is_paid = "결제완료" if header['payment_id'] is not None else "미결제"

        print(f"\n========== 주문 상세 (주문번호: {order_header_id}) ==========")
        print(f"{'상품명':<16}{'수량':<6}{'가격':<12}{'금액':<12}")
        print("-" * 46)
        for item in items:
            line_total = item['price'] * item['quantity']
            print(f"{item['product_name']:<16}{item['quantity']:<6}{item['price']:,}원{'':<4}{line_total:,}원")
        print("-" * 46)
        print(f"총 금액   : {header['total_price']:,}원")
        print(f"주문 상태 : {header['status']}")
        print(f"결제 여부 : {is_paid}")
        print("=" * 50)