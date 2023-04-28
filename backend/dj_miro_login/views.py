from django.contrib.auth.models import User

from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from allauth.socialaccount.providers.miro.views import MiroOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from .models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["text"]


class PostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]


class MiroLogin(SocialLoginView):
    adapter_class = MiroOAuth2Adapter
