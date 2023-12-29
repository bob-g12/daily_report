from django.shortcuts import render

from daily_report.models import Article
def form(request):
  Article.title = 1
  content = {
  'message': 'こんにちは！Djangoテンプレート！'
  }
  print(Article.title)
  return render(request, 'daily_report/form.html', content)

# Create your views here.

  
