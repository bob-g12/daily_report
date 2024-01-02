from django.shortcuts import render

from daily_report.models import Article

from django.views.generic import View

from django.shortcuts import redirect ,get_object_or_404

from .forms import WriteForm 

from django.forms import ModelForm
  
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
    def get(self, request, post_id):
        print("EEEE")
        post = get_object_or_404(Article, pk=post_id)
        edit_form = WriteForm(instance=post)
        return render(request, 'daily_report/edit.html', {'form': edit_form,'post':post})

    def post(self, request, post_id ,*args, **kwargs):
        post = get_object_or_404(Article, pk=post_id)
        # formに書いた内容を格納する
        form = WriteForm(request.POST, instance=post)
        # 保存する前に一旦取り出す
        post = form.save(commit=False)
        # 保存
        post.save()
        # indexのviewに移動
        return redirect(to='index')

edit = editView.as_view()

def exclude(request, post_id):
    post = get_object_or_404(Article, pk=post_id)
    post.delete()

    posts =  Article.objects.all()
    context = {
        'articles': posts,
    }
    return render(request, 'daily_report/post.html', context)
