import datetime
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import NewsLetterForm


def news_today(request):
    date = datetime.date.today()
    news = Article.todays_news()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
        else:
            form = NewsLetterForm()

    context = {
        'date': date,
        'news': news,
        'letter_form': form,
    }

    return render(request, 'news/index.html', context)


def all_news(request):
    return render(request, 'news/index.html', {
        'news': Article.objects.all(),
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
    if request.method == 'POST':
        pass

    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_articles = Article.search_by_title(search_term)
        message = f'{search_term}'
        return render(request, 'news/search.html', {
            'message': message,
            'articles': searched_articles
        })


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    return render(request, 'news/article.html', {
        'article': article
    })
