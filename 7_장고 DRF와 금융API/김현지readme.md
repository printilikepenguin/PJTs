# 주의사항

1. 오타 주의!!!!!
2. 들여쓰기 주의!!!!
```
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
```
- 여기서 serializer의 들여쓰기를 안했고, 틀려버렸어용
3. return Response() 잘 기억해주기
4. 중복제거하는 법
```
    for keys in keywords:
        value = Trend.objects.filter(name = keys.name, search_period = "all")
        if not value.exists():
```
5. 딕셔너리에서 뽑고 뽑기
```
optionlist = requests.get(url).json()['result']['optionList']
```
6. serializer 두개일 때 출력하는 법
```
    pd_serializer = DepositProductsSerializer(top_product)
    gpt_serializer = DepositOptionsSerializer(top_option)
    
    result = {
        'deposit_product': pd_serializer.data,
        'options': gpt_serializer.data
        }
```
