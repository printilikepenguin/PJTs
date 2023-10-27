from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings
import requests
from .serializers import WeatherSerializer
from .models import Weather

# Create your views here.
@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url).json()
    print(response)

    return Response(response)


@api_view(['GET'])
def save_data(request):
    api_key = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url).json()

    for li in response.get('list'):
        print(li)
        save_data = {
            'dt_txt': li.get('dt_txt'),
            'temp': li.get('main').get('temp'),
            'feels_like': li.get('main').get('feels.like'),
        }
    # 저장하기 위한 데이터를 포장
    serializer = WeatherSerializer(data=save_data)
    if serializer.is_valid():
        serializer.save()
    # 저장완료 메세지
    return JsonResponse({'message': 'okay'})
        

@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()
    # 응답할 수 있는 형태인 JSON으로 포장
    serializer = WeatherSerializer(weathers, many=True)
    return Response(serializer.data)
    # return JsonResponse({'message' : weathers})


@api_view(['GET'])
def hot_weathers(request):
    weathers = Weather.objects.all()
    hot_weathers = []
    for weather in weathers:
        # 섭씨 = 켈빈 - 273.15
        tmp = round(weather.temp - 273.15, 2)
        if tmp > 30:
            hot_weathers.append(weather)
    serializer = WeatherSerializer(hot_weathers, many=True)
    return Response(serializer.data)