from site import USER_BASE
from rest_framework import serializers

#model imports to serialize
from .models import User, Country, Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'user_description', 'user_picture']

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Country
        fields = ['name']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Post
        fields = ['poster', 'title', 'description', 'image', 'pub_date', 'latitude', 'longitude', 'country']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Comment
        fields = ['user', 'poster', 'comment_text', 'pub_date', 'nabber_points']