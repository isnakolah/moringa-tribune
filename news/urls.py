from django.urls import path, re_path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.news_today, name='news_today'),
    re_path(r'archives/(\d{4}-\d{2}-\d{2})/',
            views.past_days_news, name='past_news'),
]
