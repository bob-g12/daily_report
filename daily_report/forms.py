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
        BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
        
        widgets = {
            'day': forms.DateInput(attrs={
                "type": "date"
            }),
            "start": forms.TimeInput(attrs={
                "type": "time"
            }),
            "end": forms.TimeInput(attrs={
                "type": "time"
            }),
            'weather':forms.Select(choices=(
                ('','天気を選択'),
                ('0','晴れ'),
                ('1','曇り'),
                ('2','雨'),
                ('3','雪'),
            )),
            'name': forms.TextInput(attrs={
                'placeholder': "お名前を入力してください",
                'required' : True
                },
            ),
        }
        
        