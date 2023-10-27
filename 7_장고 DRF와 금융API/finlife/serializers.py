from rest_framework import serializers
from .models import DepositProducts, DepositOptions


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


# class DepositOptionsSerializer(serializers.ModelSerializer):
#     product = serializers.ReadOnlyField(source="DepositProducts")
#     class Meta:
#         model = DepositOptions
#         fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        # 외래키 필드는 읽기 전용으로 설정(해당 필드를 조회는 하지만, 유효성 검사 시에는 패스)
        read_only_fields = ('product',)