import datetime
from django.db import models
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(active=True, pub_date__lt=datetime.datetime.now())


class Post(models.Model):
    active = models.BooleanField(verbose_name=u'aktywny', default=False)
    pub_date = models.DateTimeField(verbose_name=u'data publikacji', null=True, blank=True)
    title = models.CharField(max_length=25, verbose_name=u'tytuł ')
    slug = models.SlugField()
    lead = models.TextField(verbose_name=u'wprowadzenie')
    body = models.TextField(verbose_name=u'treść posta')
    author = models.ForeignKey(User, verbose_name=u'autor', null=True, blank=True, on_delete=models.CASCADE)

    object = PostManager()

    class Meta:
        verbose_name = u'wpis'
        verbose_name_plural = u'wpisy'