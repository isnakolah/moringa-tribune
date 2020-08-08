import datetime
from django.db import models


class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    # Making the phone_number optional
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-first_name']


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'tags'


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateField(auto_now_add=True)
    article_image = models.ImageField(
        upload_to='articles/', blank=True, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def todays_news(cls):
        today = datetime.date.today()
        news = cls.objects.filter(pub_date=today)
        return news

    @classmethod
    def search_by_title(cls, search_term):
        search_result = cls.objects.filter(title__icontains=search_term)
        return search_result
