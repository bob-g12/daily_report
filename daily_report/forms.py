from django import forms
from .models import Article


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
        widgets = {
            'day': forms.NumberInput(attrs={
                "type": "date"
            })
        }