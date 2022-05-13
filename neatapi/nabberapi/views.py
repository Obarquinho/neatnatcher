#model imports to serialize
from .models import User, Country, Post, Comment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, CountrySerializer, PostSerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows countries to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('pub_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that llows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('pub_date')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]