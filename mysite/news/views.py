from django.shortcuts import render

from .models import Article

def index(request):
    return render(request, 'news/index.html')

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'month':month, 'article_list': a_list}
    return render(request, 'news/year_month_archive.html', context)

#every day a pk???
def article_detail(request, pk):
    a_list = Article.objects.get(id=pk)
    context = {'article': a_list}
    return render(request, 'news/detail_archive.html', context)
