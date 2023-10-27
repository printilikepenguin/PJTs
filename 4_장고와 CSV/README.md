# 판다스에서 데이터테이블 출력하기

  <tr>
  {% for column in df.columns %}
  <th>{{ column }}</th>
  {% endfor %}
  </tr>
  가로 먼저
  {% for row in df.values %}
  <tr>
    {% for value in row %}
    <td>{{ value }}</td>
    {% endfor %}
  </tr>
  {% endfor %}
  세로줄 하나 하나

# matplotlib 

### import matplotlib.pyplot as plt
matplotlib 쓸 때 x축 통일해주는 게 좋음

예제1: x, y가 같을 때
plt.plot([1,2,3,4])
plt.show()
터미널에서 실행: 파일이름 입력

참고: 이때까지 그렸던 plot 지욱
plt.clf()

예제2: x, y가 다를 때
x = [1,2,3,4]
y1 = [2,4,8,16]
plt.plot(x,y1)
plt.show()

예제3: 제목 + 각 축의 설명
y2 = [3,9,27,81]
plt.plot(x, y2)
제목
plt.title("Test Graph")
x, y축
plt.ylabel('y label')
plt.xlabel('x label')

파일로 저장하기 하려면 plt.show() 다 지워줘야함
plt.savefig('filename.png')

# numpy

pip install numpy 
pip install pandas 
pip install matplotlib 

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates

- CSV 파일 경로
csv_path = 'C:/Users/SSAFY/Desktop/pjt 2일차/Netflix_Stock_Price_Prediction/NFLX.csv'

- CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
new_df = pd.read_csv(csv_path, usecols=range(0, 5))

- 2022년 이후 데이터 필터링
df_after_2021 = new_df[new_df["Date"] >= "2021-01-01"] # 이 날부터 큰것만 뽑아라

- 출력하기
df_after_2021

- 데이터타입 조회하기
df_after_2021.dtypes 

- 날짜 데이터 변환
df_after_2021["Date"] = pd.to_datetime(df_after_2021["Date"])

df_after_2021['Date_ym'] = df_after_2021['Date'].dt.strftime("%Y-%m")
df_after_2021.head()

- 평균값
df_after_2021.groupby('Date_ym')['Close'].mean()

df_after_2021["Date_ym"] = pd.to_datetime(df_after_2021["Date_ym"])

plt.plot(df_after_2021.groupby('Date_ym')['Close'].mean())

- 그래프 그리기
plt.plot(df_after_2022['Date'], df_after_2022['High'], label='High')
plt.plot(df_after_2022['Date'], df_after_2022['Low'], label='Low')
plt.plot(df_after_2022['Date'], df_after_2022['Close'], label='Close')


- 그래프 제목 설정
plt.title('Monthly Average Close Price')

- x축 레이블 설정
plt.xlabel('Date')

- y축 레이블 설정
plt.ylabel('Average Close Price')

- x 축 설정(회전시키기) #날짜 사선으로 쓰여진 것 봐 ..
plt.xticks(rotation=45)

- 그래프에 격자 추가
plt.grid(True)
