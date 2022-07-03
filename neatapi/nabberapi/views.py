#model imports to serialize
from urllib.parse import quote_from_bytes

from django.http import HttpResponse
from .models import Picture, User, Country, Post, Comment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PictureSerializer, UserSerializer, CountrySerializer, PostSerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        pk = self.kwargs.get('pk')
        curr_user = self.queryset.filter(username=self.request.user.username).first()

        if pk == "current":
            return curr_user

        return super().get_object()

class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow user pictures to be viewed and edited
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [permissions.AllowAny]

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
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('pub_date')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
