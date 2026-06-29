import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def banapresso_menu():
    options = Options()
    options.add_argument("--start-maximized")
    url = "https://www.banapresso.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)

    action = ActionChains(driver)

    # 메뉴 > 주문하기
    first_tag = driver.find_element(By.CSS_SELECTOR, "#wrap > header > div > ul > li:nth-child(1) > a")
    second_tag = driver.find_element(By.CSS_SELECTOR, "#wrap > header > div > ul > li:nth-child(1) > ul > li:nth-child(2) > a")
    action.move_to_element(first_tag).move_to_element(second_tag).click().perform()
    print("메뉴 > 주문하기 이동 성공!")

    # html로 파서
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    menus = soup.select('ul.sc-vxg24c-3 enUhzr')
    