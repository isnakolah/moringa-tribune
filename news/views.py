import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404


def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune.')


def convert_dates(dates):
    # Function that gets the weekday number for the date
    day_number = datetime.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_news(request, past_date):
    try:
        date = datetime.datetime.strptime(past_date, '%Y-%m-%d').date()
        html = f'''
               <html>
                   <body>News for day {date.day}-{date.month}-{date.year}</body>
               </html>
               '''
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    return HttpResponse(html)


def news_of_the_day(request):
    date = datetime.date.today()

    # Function to convert date object to find exact day
    day = convert_dates(date)

    html = f'''
        <html>
            <body>
                <h1>{date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
        '''
    return HttpResponse(html)
