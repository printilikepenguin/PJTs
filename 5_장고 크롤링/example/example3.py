from bs4 import BeautifulSoup
from selenium import webdriver


def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 브라우저가 열림
    # 이때 동적인 내용들이 모두 채워진다
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 결과물 제목들을 뽑아보자
    # 1. div 태그 중 g class 를 가진 모든 요소 선택
    g_list = soup.select('div.g')
    for g in g_list:
        title = g.select_one("")
        # 결측치 처리
        if title is not None:
            print(f'제목 = {title}')

get_google_data('파이썬')