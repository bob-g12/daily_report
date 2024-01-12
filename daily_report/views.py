from django.shortcuts import render

from daily_report.models import Article

from django.views.generic import View

from django.shortcuts import redirect ,get_object_or_404

from .forms import WriteForm 

# トップページを表示する機能
class IndexView(View):
    def get(self,request):
        # 記録してある投稿の全データ
        queryset = Article.objects.all().order_by('-created_at')
        # トップページのhtmlへ記録データを乗せ移行
        return render(request, 'daily_report/post.html', {'posts': queryset})


index = IndexView.as_view()
# 投稿機能
class WriteView(View):
    # 新規入力画面へ
    def get(self, request):
        
        return render(request, 'daily_report/write.html', {'form': WriteForm})
    # 投稿機能
    def post(self, request):
        # formに書いた内容を格納する
        form = WriteForm(request.POST)
        # 保存する前に一旦取り出す
        post = form.save(commit=False)
        # 保存
        post.save()
        # トップ画面へ
        
        return redirect(to='index')
    
write = WriteView.as_view()

# 編集処理のクラス
class editView(View):
    # 編集画面を表示するための処理
    def get(self, request, post_id):
        # データベースにある対象のデータのidを一覧から引き受ける(post_id)
        # modelのArticleからid(post_id)を参照して対象のデータを取得
        post = get_object_or_404(Article, pk=post_id)
        # 入力フォームに取得したデータを埋め込んで表示
        edit_form = WriteForm(instance=post)
        # edit.htmlを表示とともに取得したデータと、それを埋め込んだフォームと送る
        return render(request, 'daily_report/edit.html', {'form': edit_form,'post':post})
    # 編集したデータを記録する処理
    def post(self, request, post_id):
        # 編集結果を編集元に反映するためにidを取得
        post = get_object_or_404(Article, pk=post_id)
        # formに書いた内容を編集元へ更新(instance=post)
        form = WriteForm(request.POST, instance=post)
        # 保存する前に一旦取り出す☆後に理解すべし!!!
        post = form.save(commit=False)
        # 保存
        post.save()
        # トップ画面へ
        return redirect(to='index')

edit = editView.as_view()

def review(request, post_id):
    return render(request, 'daily_report/delete.html',{'post_id':post_id})

#削除の機能
def exclude(request, post_id): 
    # 処理したいデータを指定
    post = get_object_or_404(Article, pk=post_id)
    # キミ消す
    post.delete()
    # トップ画面へ
    return redirect(to='index')

