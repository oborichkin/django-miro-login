"""
URL configuration for dj_miro_login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from django.http import HttpResponse

from rest_framework import routers

from .views import UserViewSet, PostsView, MiroLogin

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


@login_required
def profile(request):
    current_user = request.user
    return HttpResponse(f"<h1>Hello</h1><pre>{current_user.email}</pre>")


urlpatterns = [
    path("", include(router.urls)),
    path("me/", profile),
    path("posts/", PostsView.as_view()),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
