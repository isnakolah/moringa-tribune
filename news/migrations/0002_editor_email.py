# Generated by Django 3.1 on 2020-08-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]