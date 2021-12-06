from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse
from user.models import Profile

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    username = models.CharField(max_length=100)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    #def get_absolute_url(self):
    #    return reverse('post-detail', kwargs={'pk': self.pk})


