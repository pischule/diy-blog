from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars
from django.urls import reverse


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000)

    class Meta:
        ordering = ['user', 'bio']

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[self.id])


class Blog(models.Model):
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)

    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-datetime', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])

    @property
    def short_description(self):
        return truncatechars(self.description, 75)
