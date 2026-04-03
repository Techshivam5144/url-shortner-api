from django.db import models

class ShortUrl(models.Model):
    originalurl = models.TextField()
    shortcode = models.CharField(max_length=10,unique=True)
    createdat = models.DateTimeField(auto_now_add = True)
    clickcount = models.IntegerField(default=0)

