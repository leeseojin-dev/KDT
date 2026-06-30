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
def crawl_aladin(keyword, max_page=50):
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    all_data = []

    try:
        driver.get("https://www.aladin.co.kr/home/welcome.aspx")
        time.sleep(2)

        # 1. 검색 창 선택 > 키워드 입력
        if not keyword:
            print("[aladin] 검색어가 없습니다.")
            return []
        
        search_box = wait.until(
            EC.presence_of_element_located((By.ID, "SearchWord"))
        )
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)        
        
        for page in range(1, max_page + 1):
            # 2. 도서 영역 선택 (상위 범위) > li 태그 가져오기 (하위 범위)
            try:
                wait.until(EC.presence_of_element_located((By.ID, "Search3_Result")))
            except TimeoutException:
                pass
            books_sections = driver.find_elements(By.ID, "Search3_Result")
            if not books_sections:
                print(f"[aladin] {page}페이지에 데이터가 없어 종료합니다.")
                break
            items = books_sections[0].find_elements(By.CLASS_NAME, "ss_book_box")

            if len(items) == 0:
                print(f"[aladin] {page}페이지에 데이터가 없어 종료합니다.")
                break


            for item in items:
                try:
                    # 책제목
                    title_text = item.find_element(By.CLASS_NAME, "bo3").text.strip()
                    # 가격
                    price_text = item.find_element(By.CLASS_NAME, "ss_p2").text.strip()

                    # 저자, 출판사, 출판일 쪼개기
                    li_list = item.find_elements(By.TAG_NAME, "li")
                    author_publish_date = ""
                    for li in li_list:
                        if "|" in li.text:
                            author_publish_date = li.text.strip()
                            break
                    author_publish_date = author_publish_date.split("|")

                    # author_publish_date 리스트 안의 데이터가 2, 3개인 경우
                    if len(author_publish_date) == 3:
                        author_text = author_publish_date[0].strip().replace("(지은이)", "")
                        publish_text = author_publish_date[1].strip()
                        publish_date_text = author_publish_date[2].strip()
                    elif len(author_publish_date) == 2:
                        author_text = ""
                        publish_text = author_publish_date[0].strip()
                        publish_date_text = author_publish_date[1].strip()
                    else:
                        author_text = publish_text = publish_date_text = ""

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
                    print("[aladin] 행 처리 오류 발생!: ", e)
                
            print(f"[aladin] {page}페이지 크롤링 완료! : {len(items)}개")

            # 3. 페이지 이동
            try:
                page_buttons = driver.find_elements(By.CLASS_NAME, "numoff")
                next_btn = None
                for btn in page_buttons:
                    if btn.text.strip() == str(page + 1):
                        next_btn = btn
                        break

                if next_btn is None:
                    print(f"[aladin] {page + 1}페이지가 존재하지 않아 종료합니다.")
                    break

                driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(2)

            except Exception as e:
                print("[aladin] 다음 페이지 이동 실패!")
                break
        
        df = pd.DataFrame(all_data)
        
        if not df.empty:
            df = df.drop_duplicates(
                subset=["책제목", "저자", "가격", "출판사", "출판일"]   # 이미지
            )
            df.index = df.index + 1
        
        return df
            
    except NoSuchElementException:
        print(f"[aladin] {keyword} 검색 결과가 없어 종료합니다.")
        return []

    finally:
        driver.quit()

# crawl_aladin("핥둙셉")
# print(crawl_aladin("sqld", 3))
# crawl_aladin("sqld")