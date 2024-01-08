from django import forms
from .models import Article
from django.core.exceptions import NON_FIELD_ERRORS



class WriteForm(forms.ModelForm):
    class Meta:
        #モデルを指定
        model = Article
        #フォームとして表示したいカラムを指定
        fields = (
            'day',
            'name',
            'car_number',
            'weather',
            'start',
            'end',
            'oiling',
            'oiling2',
            'oil',
            'text'
            )
        error_messages = {
            'name':{
                'required': "名前を入力してくだちい",
            },
        }
        widgets = {
            'day': forms.DateInput(
                attrs={
                "type": "date",
                'required' : True
            }),
            'name': forms.TextInput(
                attrs={
                'placeholder': "お名前を入力してください",
                'required' : True
            }),
            'car_number': forms.TextInput(
                attrs={
                'placeholder': "例)88-88",
                'required' : True
            }),
            "start": forms.TimeInput(
                attrs={
                "type": "time",
                'required' : True
            }),
            "end": forms.TimeInput(
                attrs={
                "type": "time",
                'required' : True
            }),
            'weather':forms.Select(
                choices=(
                ('','天気を選択'),
                ('0','晴れ'),
                ('1','曇り'),
                ('2','雨'),
                ('3','雪'),
                ),
                attrs={
                'required' : '天気を選択'
            }),
        }
        
        