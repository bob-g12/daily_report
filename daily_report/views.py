from django.shortcuts import render

def form(request):
  content = {
  'message': 'こんにちは！Djangoテンプレート！'
  }
  return render(request, 'daily_report/form.html', content)
# Create your views here.
