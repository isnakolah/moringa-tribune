import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


def welcome(request):
    return render(request, 'news/welcome.html', {
        'date': datetime.datetime.now()
    })


def past_days_news(request, past_date):

    try:
        date = datetime.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == datetime.date.today():
        return redirect(news_of_the_day)

    return render(request, 'news/past-news.html', {
        'date': date,
    })


def news_of_the_day(request):
    date = datetime.date.today()

    return render(request, 'news/today', {
        'date': date,
    })
