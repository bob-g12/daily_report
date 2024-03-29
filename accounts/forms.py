from django import forms
from django.contrib.auth.models import User
from .models import Account

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username',)#'email','password'「メールの項目追加」
        # フィールド名指定
        labels = {'username':"ユーザーID",}#'email':"メール"「メール、パスワードの項目追加」

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name',)#'account_image',「写真の項目追加」
        labels = {'last_name':"苗字",'first_name':"名前",}#'account_image':"写真アップロード",「写真の項目追加」
        
#AddAccountFormとadd_account_formのコメントアウトをすべて外すと苗字、名前を追加
