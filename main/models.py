from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your models here.

fs = FileSystemStorage(location=settings.MEDIA_ROOT + "/articles-img/")

class Author(models.Model):
    user = models.OneToOneField(User)
    nationality = models.CharField(max_length = 32,
                                  default = "")
    def __unicode__(self):
        return self.user.__unicode__()

class Post(models.Model):
    title = models.CharField("Titulo",
                            max_length = 32)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    publicated = models.BooleanField(default = True)
    author = models.ForeignKey(Author)

    image = models.ImageField(storage=fs)


    '''image = models.FilePathField(path= "~/Descargas",
                                match = "/.+(\.png$|\.jpeg$|\.jpg$)/",
                                default="")
    '''


    def image_name(self):
        return os.path.basename(self.image.name)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User,
                                 null = True,
                                 blank = True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey(Post)
    approved = models.BooleanField(default = False)
