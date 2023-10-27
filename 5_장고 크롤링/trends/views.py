from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm, TrendForm
from bs4 import BeautifulSoup
from selenium import webdriver
import re


# Create your views here.
def keyword(request):
    # 키워드 저장 및 keyword.html 렌더링
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            keywords = form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
        keywords = Keyword.objects.all()
    context = {
        'form' : form,
        'keywords' : keywords,
    }
    return render(request, 'trends/keyword.html', context)


def keyword_detail(request, pk):
    # 키워드 삭제 및 keyword.html로 리다이렉션
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 브라우저가 열림
    # 이때 동적인 내용들이 모두 채워진다
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 검색결과 가져오기 '> # .'
    # div 태그 안의 id가 result-stats 라는 요소
    result_stats = soup.select_one("div#result-stats")
    print(result_stats.text)
    return result_stats.text


def crawling(request):
    # 크롤링 수행 및 crawling.html 렌더링
    keywords = Keyword.objects.all()
    trends = Trend.objects.all()
    trends_list = []
    for k in keywords:
        value = Trend.objects.filter(name = k.name, seach_period = "all")
        if not value.exists():
          searching_counts = str(re.sub(r'[^0-9]', '', get_google_data(k.name)))
          searching_counts = int(searching_counts[:-2])
          trend = Trend(name=k.name, result=searching_counts, seach_period='all')
          trends_list.append(trend)
    Trend.objects.bulk_create(trends_list)
    
    Trend_form = TrendForm()
    
    context = {
        'form' : Trend_form,
        'trends' : trends
    }

    return render(request, 'trends/crawling.html', context)


def crawling_histogram(request):
    # 크롤링 수행후 수행결과 막대그래프 생성 및
    return render(request, 'crawling_histogram.html')


def crawling_advanced(request):
    # 지난 1년 기준 크롤링 수행 후 수행결과 막대그래프생성및 crawling
    return render(request, 'crawling_advanced.html')