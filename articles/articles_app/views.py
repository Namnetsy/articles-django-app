from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage
from .models import Article

import re

def index(request):
    if request.method == 'GET' and 'page' in request.GET:
        try:
            page = int(request.GET['page'])
        except ValueError as e:
            print(e)

    paginator = Paginator(Article.objects.all(), 3, allow_empty_first_page=True)

    try:
        articles = paginator.page(page if 'page' in locals() else 1).object_list
    except EmptyPage as e:
        print(e)
        raise Http404

    for article in articles:
        article.preview = clean_html(article.content)[:200]

        if len(article.content) > 200:
            article.preview += '...'

    ctx = {
        'articles': articles,
        'page_count': range(1, paginator.num_pages + 1),
        'current_page': page if 'page' in locals() else 1
    }

    return render(request, 'articles_app/index.html', ctx)


def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)

    return render(request, 'articles_app/view_article.html', { 'article': article })


def error_404_view(request, exception):
    return render(request, 'articles_app/error_404.html')


def clean_html(html):
    regex = re.compile('<.*?>')

    return re.sub(regex, '', html)
