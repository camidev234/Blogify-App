from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categorie(models.Model):
    categorie = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Article(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    response = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_responses', through='Like')
    dislikes = models.ManyToManyField(User, related_name='disliked_responses', through='Dislike')

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.ForeignKey(UserResponse, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'response')
        
class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.ForeignKey(UserResponse, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'response')