from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class News(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cover_picture = models.ImageField(upload_to="news_pictures/", default="default.jpg")
    background_picture = models.ImageField(upload_to="news_pictures/", default="default.jpg")
    news_slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

