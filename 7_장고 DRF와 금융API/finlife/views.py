from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Max
import requests

API_KEY = settings.API_KEY
BASE_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'


@api_view(['GET'])
# GET: requests로 정기예금상품목록 조회 -> 정기예금 상품목록과 옵션 목록 DB에 저장
def save_deposit_products(request):
    url = BASE_URL + f'depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    baselist = requests.get(url).json()['result']['baseList']
    optionlist = requests.get(url).json()['result']['optionList']
    
    for li in baselist:
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
        }
        # 저장하기 위한 데이터를 포장
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid():
            serializer.save()

    for li in optionlist:
        save_data = {
            'product': li.get('product'),
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'intr_rate' : li.get('intr_rate'),
            'intr_rate2' : li.get('intr_rate2'),
            'save_trm' : li.get('save_trm'),
        }
        # 저장하기 위한 데이터를 포장
        serializer = DepositOptionsSerializer(data=save_data)

        if serializer.is_valid(raise_exception=True):
            product = DepositProducts.objects.get(fin_prdt_cd=save_data.get('fin_prdt_cd'))
            serializer.save(product=product)
            
    return Response({'message': 'okay'})


@api_view(['GET', 'POST'])
# GET: 전체 정기예금 상품목록반환, POST: 상품 데이터 저장
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# GET: 특정 상품의 옵션리스트 반환
def deposit_product_options(request, fin_prdt_cd):
    product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# GET: 가입기간과 상관X, 최고금리상품과 해당 상품의 옵션리스트 출력
def top_rate(request):   

    # 최고우대금리 변수 : intr_rate2 -> 제일 높은 값 찾기
    max_intr_rate2 = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))
    target = max_intr_rate2.get('intr_rate2')

    # 금리가 제일 높은 옵션 찾아오기
    top_option = DepositOptions.objects.filter(intr_rate2 = target).first()
    top_product = DepositProducts.objects.get(pk = top_option.product_id)

    pd_serializer = DepositProductsSerializer(top_product)
    gpt_serializer = DepositOptionsSerializer(top_option)
    
    result = {
        'deposit_product': pd_serializer.data,
        'options': gpt_serializer.data
        }

    return Response(result)
