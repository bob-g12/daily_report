from django.shortcuts import render

from daily_report.models import Article

from django.views.generic import View

from django.shortcuts import redirect

from .forms import WriteForm
  
class IndexView(View):
    def get(self,request):
        
        queryset = Article.objects.all().order_by('-created_at')

        return render(request, 'daily_report/post.html', {'posts': queryset})


index = IndexView.as_view()

class WriteView(View):
    def get(self, request):
        return render(request, 'daily_report/write.html', {'form': WriteForm})

    def post(self, request, *args, **kwargs):
        # formに書いた内容を格納する
        form = WriteForm(request.POST)
        # 保存する前に一旦取り出す
        post = form.save(commit=False)
        # 保存
        post.save()
        # indexのviewに移動
        return redirect(to='index')
    
write = WriteView.as_view()

class editView(View):
    def get(self, request):
        return render(request, 'daily_report/edit.html', {'form': WriteForm})

    def post(self, request, *args, **kwargs):
        # formに書いた内容を格納する
        form = WriteForm(request.POST)
        # 保存する前に一旦取り出す
        post = form.save(commit=False)
        # 保存
        post.save()
        # indexのviewに移動
        return redirect(to='index')

edit = editView.as_view()