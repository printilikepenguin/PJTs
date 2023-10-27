from django.db import models

# Create your models here.
class Keyword(models.Model):
    name = models.CharField(max_length=20)
    # 검색할 키워드명
    created_at = models.DateTimeField(auto_now_add=True)
    # 추가된 날짜

class Trend(models.Model):
    name = models.TextField()
    result = models.PositiveIntegerField()
    # 검색 결과 수
    seach_period = models.TextField()
    # 검색 기간
    created_at = models.DateTimeField(auto_now_add=True)