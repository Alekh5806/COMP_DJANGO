"""
URL configuration for chaihq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_tweet, name='tweet_create'),
    path('<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('<int:tweet_id>/edit/', views.edit_tweet, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name='tweet_delete'),
    path('register/', views.register, name='register'),
]
