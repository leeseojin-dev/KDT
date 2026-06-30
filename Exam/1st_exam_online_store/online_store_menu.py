from online_store_service import OnlineStoreService

class Menu:
    def __init__(self):
        self.service = OnlineStoreService()

    def run(self):
        while True:
            print("\n")
            print("==========================")
            print("\t온라인스토어")
            print("==========================")
            print("1. 회원 가입")
            print("2. 로그인")
            print("0. 프로그램 종료")
            menu = input("메뉴 번호를 선택하세요: ")
            if not menu.isdigit():
                print("0~2 범위의 숫자를 입력하세요")
                continue
            menu = int(menu)

            if menu == 0:
                print("프로그램을 종료합니다")
                break
            elif menu == 1:
                self.sign_up_menu()
            elif menu == 2:
                should_exit = self.sign_in_menu()   # 반환값을 받음
                if should_exit:
                    break   
            else:
                print("0~2 범위의 숫자를 입력하세요")

    def main_menu(self):
        while True:
            print("\n")
            print("==========================")
            print("\t메인 메뉴")
            print("==========================")
            print("1. 상품 목록 조회")
            print("2. 상품 검색")
            print("3. 주문하기")
            print("4. 주문 내역 조회")
            print("5. 로그아웃")
            print("0. 프로그램 종료")
            menu = input("메뉴 번호를 선택하세요: ")
            if not menu.isdigit():
                print("0~2 범위의 숫자를 입력하세요")
                continue
            menu = int(menu)

            if menu == 0:
                print("프로그램을 종료합니다")
                return True
            elif menu == 1:
                print("==========================")
                print("상품 목록을 출력합니다")
                self.service.show_product()

            elif menu == 2:
                print("==========================")
                self.service.search_product()
            
            elif menu == 3:
                print("==========================")
                print("상품 주문을 시작합니다")
                self.service.order_product()
                            
            elif menu == 4:
                print("==========================")
                print("주문 내역을 출력합니다")
                self.service.show_order_list()
                
            elif menu == 5:
                self.service.logout()
                return False

            else:
                print("0~5 범위의 숫자를 입력하세요")

    def sign_up_menu(self):
            self.service.signup()

    def sign_in_menu(self):
        self.service.login()
        if self.service.current_user is not None:
            return self.main_menu()   # main_menu()의 반환값을 그대로 위로 전달
        return False
    