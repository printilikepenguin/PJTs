## 웹크롤링
여러 웹 페이지를 돌아다니며 원하는 정보를 모으는 기술

## 웹크롤링 프로세스
1. 웹페이지 다운로드
- 해당 웹페이지의 html, css, javascript 등의 코드를 가져오는 단계
2. 페이지 파싱
- 다운로드 받은 코드를 분석하고 필요한 데이터를 추출하는 단계
3. 링크 추출 및 다른 페이지 탐색
- 다른 링크를 추출하고, 다음 단계로 이동하여 원하는 데이터를 추출하는 단계
4. 데이터 추출 및 저장
- 분석 및 시각화에 사용하기 위해 데이터를 처리하고 저장하는 단계

## 필수 라이브러리


## 많이 쓰이는 함수 4개
1. 태그로 검색하기
  1.1 가장 첫번째 태그에 해당하는 요소
    크롤링할 때는 항상 페이지 분석 -> 검색
    title = soup.find('a')
    print(f'제목 : {title}')
    print(f'제목 : {title.text}')

  1.2 해당 태그 모든 요소
    a_tags = soup.find_all('a')
    print(f'a 태그들 = {a_tags}') # 리스트 형태로 반환됨
    for a_tag in a_tags:
        print(f'링크 : {a_tag}')

2. CSS 선택자로 검색하기
    2.1 첫번재로 css 선택자와 일치하는 요소
    word = soup.select_one('.text')
    print(f'첫 번째 글 = {word.text}')

  2.2 css 선택자와 일치하는 모든 요소
    words = soup.select('.text')
    for w in words:
        print(f'글 = {w.text}')

유저 에이전트