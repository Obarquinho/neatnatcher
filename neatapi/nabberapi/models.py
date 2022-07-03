import datetime
from operator import mod

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User as DefaultUser

# true fun stuff

class Picture(models.Model):
    # https://stackoverflow.com/questions/5517950/django-media-url-and-media-root
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.image.name

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    # not to sure how to store password in db, hashing seems to be suggested
    password = models.CharField(max_length=256)
    user_fname = models.TextField()
    user_lname = models.TextField()
    user_picture = models.ForeignKey(Picture, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

# honestly don't really care for a country but having it there because idk
class Country(models.Model):
    name = models.CharField(max_length=56)
    def __str__(self):
        return self.name

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    #description = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ForeignKey(Picture, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    #reasoning for latitude and longitude is from stack overflow post
    #https://stackoverflow.com/questions/1196415/what-datatype-to-use-when-storing-latitude-and-longitude-data-in-sql-databases
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    # like reddit karma
    nabber_points = models.SmallIntegerField()

    def __str__(self):
        return self.comment_text

