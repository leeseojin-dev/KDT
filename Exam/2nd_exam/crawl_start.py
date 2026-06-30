from crawl_yes24 import crawl_yes24
from crawl_kyobo import crawl_kyobo
from crawl_aladin import crawl_aladin
import pandas as pd
import time

def crawl_start(keyword, n1, n2, n3):

    # yes24
    yes24_start = time.perf_counter()
    yes24_data = crawl_yes24(keyword, n1)
    yes24_end = time.perf_counter()
    yes24_time = yes24_end - yes24_start

    # kyobo
    kyobo_start = time.perf_counter()
    kyobo_data = crawl_kyobo(keyword, n2)
    kyobo_end = time.perf_counter()
    kyobo_time = kyobo_end - kyobo_start

    # aladin
    aladin_start = time.perf_counter()
    aladin_data = crawl_aladin(keyword, n3)
    aladin_end = time.perf_counter()
    aladin_time = aladin_end - aladin_start

    print(f"yes24 크롤링 시간: {yes24_time}초")
    print(f"kyobo 크롤링 시간: {kyobo_time}초")
    print(f"aladin 크롤링 시간: {aladin_time}초")
    print(f"전체 크롤링 시간: {yes24_time + kyobo_time + aladin_time}초")

    with pd.ExcelWriter(f"crawling_{keyword}_search_list.xlsx", mode='w') as writer:
        yes24_data.to_excel(writer, sheet_name="yes24", index=False)
        kyobo_data.to_excel(writer, sheet_name="kyobo", index=False)
        aladin_data.to_excel(writer, sheet_name="aladin", index=False)

    print(f"crawling_{keyword}_search_list.xlsx 명으로 엑셀 저장 완료!")

crawl_start("sqld", 2, 2, 1)