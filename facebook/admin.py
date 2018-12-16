from django.contrib import admin

# Register your models here.
from facebook.models import Article
from facebook.models import Trya
from facebook.models import Page
from facebook.models import Comment
from facebook.models import Like



admin.site.register(Article)
admin.site.register(Trya)
admin.site.register(Page)
admin.site.register(Comment)
admin.site.register(Like)



