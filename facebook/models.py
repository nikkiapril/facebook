from django.db import models
from django.conf import settings


# facebook model
class Article(models.Model):
    author      = models.CharField(max_length=120)
    title       = models.CharField(max_length=120)
    text        = models.TextField()
    password    = models.CharField(max_length=120)
    total_like        = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True) #자동날짜
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like', default='')
    
    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# week4
class Page(models.Model):
    master = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 자동날짜

    def __str__(self):
        return self.name

# week4-1
class Try(models.Model):
     master = models.CharField(max_length=120)
     name = models.CharField(max_length=120)
     text = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.name

# week4-2
class Trya(models.Model):
     master = models.CharField(max_length=120)
     writer = models.CharField(max_length=120)
     title = models.CharField(max_length=120)
     content = models.TextField()
     date = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.writer

#week6 : Comment Model
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author  = models.CharField(max_length=120)
    text    = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

# Like Model
