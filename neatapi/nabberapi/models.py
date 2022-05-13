import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# true fun stuff

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    # not to sure how to store password in db, hashing seems to be suggested
    password = models.CharField(max_length=256)
    user_description = models.TextField()
    user_picture = models.ImageField()
    def __str__(self):
        return self.username

class Country(models.Model):
    name = models.CharField(max_length=56)
    def __str__(self):
        return self.name

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    #description = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField()
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
    nabber_points = models.SmallIntegerField()

    def __str__(self):
        return self.comment_text

# stuff I have here for reference
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

