# Generated by Django 3.1 on 2021-04-12 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_auto_20210307_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='slug',
            new_name='news_slug',
        ),
    ]
