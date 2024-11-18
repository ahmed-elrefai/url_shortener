from django.db import models

# Create your models here.


class UrlInfo(models.Model):
    url = models.CharField('Url', max_length=200)
    short_url = models.CharField('Shortened Url', max_length=50)
    def __str__(self):
        return self.short_url

