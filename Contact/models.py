from django.db import models


class Contact(models.Model):
    last_name = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=256, blank=False)
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
