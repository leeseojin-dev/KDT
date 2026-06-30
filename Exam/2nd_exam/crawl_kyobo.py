import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# yes24 크롤링 함수
def crawl_kyobo(keyword, max_page=50):
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    all_data = []

    try:
        driver.get("http://www.kyobobook.co.kr/")
        time.sleep(2)

        # 1. 검색 창 선택 > 키워드 입력
        if not keyword:
            print("[kyobo] 검색어가 없습니다.")
            return []
        
        search_box = wait.until(
            EC.presence_of_element_located((By.ID, "searchKeyword"))
        )
        search_box.clear()

        # 입력 시 키워드가 깨지는 문제
        for ch in keyword:
            search_box.send_keys(ch)
            time.sleep(0.2)

        search_box.send_keys(Keys.ENTER)
        time.sleep(2)        

        try:
            driver.find_element(By.CSS_SELECTOR, "#shopData_list > ul")
        except NoSuchElementException:
            print(f"[kyobo] {keyword} 검색 결과가 없습니다.")
            return []
        
        for page in range(1, max_page + 1):
            # 2. 도서 영역 선택 (상위 범위) > li 태그 가져오기 (하위 범위)
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.prod_area.horizontal")))
            except TimeoutException:
                pass
            books_sections = driver.find_elements(By.CSS_SELECTOR, "#shopData_list > ul")
            if not books_sections:
                print(f"[kyobo] {page}페이지에 데이터가 없어 종료합니다.")
                break
            items = books_sections[0].find_elements(By.CSS_SELECTOR, "div.prod_area.horizontal")

            if len(items) == 0:
                print(f"[kyobo] {page}페이지에 데이터가 없어 종료합니다.")
                break

            for item in items:
                try:
                    # 책제목
                    title_text = item.find_element(By.CLASS_NAME, "prod_info").text.strip()
                    # 저자
                    author_text = item.find_element(By.CSS_SELECTOR, "div.prod_info_box > div.prod_author_info > div.auto_overflow_wrap.prod_author_group > div.auto_overflow_contents > div > a.author.rep").text.strip()
                    # 가격
                    # if not price:
                    #     outofprint = item.find_element(By.CLASS_NAME, "prod_purchase_state").text.strip()
                    #     if outofprint:
                    #         price_text = "절판"
                    try:
                        price = item.find_element(By.CLASS_NAME, "price").text.strip()
                        if price == "무료도서":
                            price_text = "0원"
                        else:
                            price_text = price
                    except NoSuchElementException:
                        price_text = "절판된 도서"
                    

                    # 출판사
                    publish_text = item.find_element(By.CSS_SELECTOR, "div.prod_info_box > div.prod_author_info > div.prod_publish > a").text.strip()
                    # 출판일
                    publish_date_text = item.find_element(By.CSS_SELECTOR, "div.prod_info_box > div.prod_author_info > div.prod_publish > span.date").text.strip()
                    # 이미지❗

                    if title_text:
                        all_data.append({
                            "검색어": keyword,
                            "책제목": title_text,
                            "저자": author_text,
                            "가격": price_text,
                            "출판사": publish_text,
                            "출판일": publish_date_text
                            # "이미지": author_text,
                        })
                except Exception as e:
                    print("[kyobo] 행 처리 오류 발생!: ", e)
                
            print(f"[kyobo] {page}페이지 크롤링 완료! : {len(items)}개")
            next_start_index = page * 20 + 1

            # 3. 페이지 이동
            try:
                page_buttons = driver.find_elements(By.CSS_SELECTOR, "a.btn_page_num")
                next_btn = None
                for btn in page_buttons:
                    if btn.text.strip() == str(page + 1):
                        next_btn = btn
                        break

                if next_btn is None:
                    print(f"[kyobo] {page + 1}페이지가 존재하지 않아 종료합니다.")
                    break

                driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(2)

            except Exception as e:
                print("[kyobo] 다음 페이지 이동 실패!: ", e)
                break

        df = pd.DataFrame(all_data)
        
        if not df.empty:
            df = df.drop_duplicates(
                subset=["책제목", "저자", "가격", "출판사", "출판일"]   # 이미지
            )
            df.index = df.index + 1
        
        return df
            
    except NoSuchElementException:
        print(f"[kyobo] {keyword} 검색 결과가 없어 종료합니다.")
        return []

    finally:
        driver.quit()

# crawl_kyobo("핥둙셉")
# print(crawl_kyobo("sqld"))
# crawl_kyobo("sqld")