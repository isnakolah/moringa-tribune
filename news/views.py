import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Article


def news_today(request):
    date = datetime.date.today()
    news = Article.todays_news()
    return render(request, 'news/index.html', {
        'date': date,
        'news': news
    })


def past_days_news(request, past_date):

    try:
        date = datetime.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == datetime.date.today():
        return redirect(news_today)

    return render(request, 'news/past-news.html', {
        'date': date,
    })


def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_articles = Article.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'news/search.html', {
            'message': message,
            'articles': searched_articles
        })
