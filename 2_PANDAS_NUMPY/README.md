##excel이 아닌 pandas 사용이유
1. 사용성
2. 방대한 양의 데이터 처리에 대한 속도
3. 인공지능 활용 -> 머신러닝, 딥러닝


#pip install pandas
- 데이터 분석 라이브러리 표 형식 (행x열) 
- 데이터 다루는데 사용 
- csv, json 파일 읽고 쓰는게 목적

#pip install matplotlib
- 데이터 분석결과를 시각화

# pip install numpy
- 훨씬 빠른 연산이 가능

#프로세스
1. 결측값 제거
2. 데이터 수집
3. 데이터 전처리 (헤더변경, 단위변환 등)
4. 데이터 분석
5. 결과 해석 및 공유

#x축 간격 조정법
import matplotlib.dates as dates
import matplotlib.date as mdates
from datetime import datetime

ax = plt.gca()
ax.xaxis.set_major_locator(dates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(dates.DateFormatter("%Y-%m"))

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 2, 28)
ax.set_xlim(start_date, end_date)

#x축 날짜 단축
df_after_2022["Date"] = pd.to_datetime(df_after_2022["Date"])
df_after_2022.dtypes
datetime 등록하고 계속 돌려주면 됨

df = pd.read_csv('data/test_data.CSV', encoding='cp949')
df.head()
이것도 등록하면 표 계속 돌아감
