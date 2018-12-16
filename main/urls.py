"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from facebook.views import play
from facebook.views import play2
from django.contrib import admin
from django.urls import path
from facebook.views import profile
from facebook.views import tryrr
from facebook.views import fail
from facebook.views import warn
from facebook.views import help
from facebook.views import multiple
from facebook.views import newsfeed
from facebook.views import trynewsfeed
from facebook.views import detail_feed
from facebook.views import new_feed
from facebook.views import remove_feed
from facebook.views import edit_feed
from facebook.views import new_page
from facebook.views import pages
from facebook.views import edit
from facebook.views import remove
from facebook.views import like_button
from facebook.views import post_like
from facebook.views import comment_write
from facebook.views import remove_comment
from facebook.views import edit_comment
from facebook.views import search_list
from facebook.views import main
from facebook.views import bora
urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', play),
    path('play2/', play2),
    path('myname/profile/',profile ),
    path('board/tryrr/', tryrr),
    path('fail/', fail),
    path('help/', help),
    path('warn/', warn),
    path('multiple/', multiple),
    path('trynewsfeed/',trynewsfeed),

    path('new/', new_feed),
    path('main/', newsfeed),
    path('bora/', bora),
    path('', main),
    path('search/<author>/',search_list),
    path('feed/<pk>/',detail_feed),
    path('like', post_like),
    path('feed/<pk>/remove',remove_feed),
    path('feed/<pk>/remove_comment',remove_comment),
    path('feed/<pk>/edit',edit_feed),
    path('feed/<pk>/edit_comment',edit_comment),

    path('pages/', pages),
    path('pages/new/',new_page),
    path('pages/add/',new_page),
    path('pages/edit/',edit),
    path('pages/remove/',remove),
    path('comment_write',comment_write),

]