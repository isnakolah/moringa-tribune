from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.news_today, name='news_today'),
    re_path(r'archives/(\d{4}-\d{2}-\d{2})/',
            views.past_days_news, name='past_news'),
    path('search/', views.search_results, name='search_results'),
    path('all-news/', views.all_news, name='all_news'),
    path('article/<int:article_id>', views.article, name='article')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
