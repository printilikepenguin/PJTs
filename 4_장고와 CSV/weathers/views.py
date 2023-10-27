from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO
plt.switch_backend('Agg')
csv_path = 'weathers/data/austin_weather.csv'

def index(request):
    return render(request, 'weathers/index.html')

# pandas dataframe으로 데이터 출력
def problem1(request):
    df = pd.read_csv(csv_path)
    context = {'df' : df}
    return render(request, 'weathers/problem1.html', context)

# 일 별 온도 비교를 위한 라인 그래프 출력
def problem2(request):
    columns = ['Date', 'TempHighF', 'TempAvgF', 'TempLowF']
    df = pd.read_csv(csv_path, usecols=columns)
    df['Date'] = pd.to_datetime(df['Date'])

    plt.clf()
    # 그래프 먼저 3개 그려주기
    plt.plot(df.Date, df.TempHighF, label='High Temperature')
    plt.plot(df.Date, df.TempAvgF, label='Average Temperature')
    plt.plot(df.Date, df.TempLowF, label='Low Temperature')

    plt.title('Temperature Variation')  # 제목
    plt.ylabel('Temperature (Fahrenheit)')  
    plt.xlabel('Date')
    # plt.xticks(rotation=45)
    plt.grid(True)  # 격자추가
    plt.legend(loc='lower center')  # 범례설정

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart_img' : f'data:image/png;base64,{img_base64}',
    }
    return render(request, 'weathers/problem2.html', context)

# 월 별 온도 비교를 위한 라인 그래프 출력
def problem3(request):
    columns = ['Date', 'TempHighF', 'TempAvgF', 'TempLowF']
    df = pd.read_csv(csv_path, usecols=columns)
    df['Date'] = pd.to_datetime(df['Date'])
    # 월 별 온도 평균을 위해 숫자 형식으로 변환, 평균 구하기
    # 1. 날짜 월 별로 자른 인덱스 만들기
    df['Date_ym'] = df['Date'].dt.strftime('%Y-%m')
    # 2. 평균값 만들어주기
    montyly_avg = df.groupby('Date_ym')[['TempHighF', 'TempAvgF', 'TempLowF']].mean()
    df = df.drop_duplicates(subset=['Date_ym'])
    df['Date_ym'] = pd.to_datetime(df['Date_ym'])
    
    plt.clf()
    # 그래프 3개 그려주기
    plt.plot(df.Date_ym, montyly_avg['TempHighF'], label='High Temperature')
    plt.plot(df.Date_ym, montyly_avg['TempAvgF'], label='Average Temperature')
    plt.plot(df.Date_ym, montyly_avg['TempLowF'], label='Low Temperature')

    plt.title('Temperature Variation')  # 제목
    plt.ylabel('Temperature (Fahrenheit)')  
    plt.xlabel('Date')
    # plt.xticks(rotation=45)
    plt.grid(True)  # 격자추가
    plt.legend(loc='lower center')  # 범례설정

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart_img' : f'data:image/png;base64,{img_base64}',
    }
    return render(request, 'weathers/problem3.html', context)

# 기상현상발생횟수 히스토그램 출력
def problem4(request):
    columns = ['Date', 'Events']
    df = pd.read_csv(csv_path, usecols=columns)
    event_list = df["Events"].to_list()
    weather_dict = {
        "No Events" : 0,
        "Rain" : 0,
        "Thunderstorm" : 0,
        "Fog" : 0,
        "Snow" : 0,
    }
    for i in event_list:
        if i == " ":
            weather_dict["No Events"] += 1
        else:
            i = i.split(", ")
            for j in i:
                j = j.strip()
                weather_dict[j] += 1
    x = weather_dict.keys()
    y = weather_dict.values()

    plt.clf()
    plt.figure(figsize=(12, 8))
    plt.bar(x, y)
    plt.legend(loc = "upper right")
    plt.title("Event Counts")
    plt.xlabel("Events")
    plt.ylabel("Count")
    plt.grid(True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        'chart_img' : f'data:image/png;base64,{image_base64}'
    }

    return render(request, "weathers/problem4.html", context)