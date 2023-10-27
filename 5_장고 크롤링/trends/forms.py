from django import forms
from .models import Keyword, Trend

class KeywordForm(forms.ModelForm):
    name = forms.CharField(
        label='키워드'
    )
    
    class Meta:
        model = Keyword
        fields = '__all__'

class TrendForm(forms.ModelForm):
    name = forms.CharField(
        label='검색결과'
    )
    class Meta:
        model = Trend
        fields = '__all__'


        