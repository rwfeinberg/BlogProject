from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Defines post model used on blog app
class Post(models.Model):

    # Fields of a post
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):                                              # Overriden function to return post when called
        return self.title

    def get_absolute_url(self):                                     # Overriden function to direct to new post location when first created
        return reverse('post-detail', kwargs={'pk': self.pk})