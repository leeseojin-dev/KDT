import time
import pandas as pd
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# yes24 크롤링 함수
def crawl_yes24(keyword, max_page=50):
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    all_data = []

    try:
        driver.get("https://www.yes24.com/Main/default.aspx")
        time.sleep(2)

        # 1. 검색 창 선택 > 키워드 입력
        if not keyword:
            print("[yes24] 검색어가 없습니다.")
            return []
        
        search_box = wait.until(
            EC.presence_of_element_located((By.ID, "query"))
        )
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)        
        
        for page in range(1, max_page + 1):
            # 2. 도서 영역 선택 (상위 범위) > li 태그 가져오기 (하위 범위)
            books_section = driver.find_element(By.ID, "goodsListWrap")
            items = books_section.find_elements(By.CSS_SELECTOR, "li[data-goods-no]")

            if len(items) == 0:
                print(f"[yes24] {page}페이지에 데이터가 없어 종료합니다.")
                break

            for item in items:
                try:
                    # 책제목
                    title_text = item.find_element(By.CLASS_NAME, "gd_name").text.strip()
                    # 저자
                    author_text = item.find_element(By.CSS_SELECTOR, "div > div.item_info > div.info_row.info_pubGrp > span.authPub.info_auth > a").text.strip()
                    # 가격
                    price_text = item.find_element(By.CLASS_NAME, "txt_num").text.strip()
                    # 출판사
                    publish_text = item.find_element(By.CSS_SELECTOR, "div > div.item_info > div.info_row.info_pubGrp > span.authPub.info_pub > a").text.strip()
                    # 출판일
                    publish_date_text = item.find_element(By.CSS_SELECTOR, "div > div.item_info > div.info_row.info_pubGrp > span.authPub.info_date").text.strip()
                    # 이미지
                    image_path = ""
                    try:
                        
                        image_url = item.find_element(By.TAG_NAME, "img").get_attribute("src")
                        save_folder = "./images/yes24"

                        response = requests.get(image_url, stream=True)     # 이미지 다운로드 요청
                        
                        content_type = response.headers.get("Content-Type")
                        content_type = content_type.split("/")[-1]

                        if not os.path.exists(save_folder):
                            os.makedirs(save_folder)
                        file_name = image_url.split("/")[-2]
                        image_path = f"{save_folder}/{file_name}.{content_type}"

                        if response.status_code == 200:
                            with open(image_path, 'wb') as file:
                                for chunk in response.iter_content(1024):
                                    file.write(chunk)
                        else:
                            print("이미지를 다운로드할 수 없습니다.")
                    except Exception as e:
                        print("[yes24] 이미지 다운로드 오류 발생!: ", e)

                    if title_text:
                        all_data.append({
                            "검색어": keyword,
                            "책제목": title_text,
                            "저자": author_text,
                            "가격": price_text,
                            "출판사": publish_text,
                            "출판일": publish_date_text,
                            "이미지": image_path
                        })
                except Exception as e:
                    print("[yes24] 행 처리 오류 발생!: ", e)
                
            print(f"[yes24] {page}페이지 크롤링 완료! : {len(items)}개")

            # 3. 페이지 이동
            try:
                next_btns = driver.find_elements(By.CSS_SELECTOR, f"a.num[title='{page + 1}']")
                if not next_btns:
                    print(f"[yes24] {page +  1}페이지가 존재하지 않아 종료합니다.")
                    break
                next_btns[0].click()
                time.sleep(2)

            except Exception as e:
                print("[yes24] 다음 페이지 이동 실패!")
                break
        
        # 4. 데이터프레임 변환
        df = pd.DataFrame(all_data)
        
        if not df.empty:
            df = df.drop_duplicates(
                subset=["책제목", "저자", "가격", "출판사", "출판일", "이미지"]
            )
            df.index = df.index + 1
        
        return df
            
    except NoSuchElementException:
        print(f"[yes24] {keyword} 검색 결과가 없어 종료합니다.")
        return []

    finally:
        driver.quit()

# crawl_yes24("핥둙셉")
# print(crawl_yes24("sqld", 1))
# crawl_yes24("sqld")