# Generated by Django 3.1 on 2021-03-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Animal', '0003_auto_20210301_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='vaccines',
            field=models.ManyToManyField(to='Animal.Vaccine'),
        ),
    ]
