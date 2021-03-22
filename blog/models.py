from django.db import models
from datetime import date
from django.urls import reverse
from datetime import datetime


class Author(models.Model):
    """
    Add name of author for post
    """
    auth_name = models.CharField(max_length=100)
    auth_last_name = models.CharField(max_length=150)
    nick_name = models.CharField(max_length=100)
    register_date = models.DateTimeField(auto_now_add=True, blank=False)
    published = models.DateField(null=True, blank=True)
    objects = models.Manager()

    class Meta:
        """
        Present titles list
        """
        ordering = ["published", "register_date", "nick_name"]

    def get_absolute_url(self):
        """
        Receive list with all titles
        """
        return reverse('post-detail', args=[str(self.nick_name)])


class Post(models.Model):
    """
    Show posts
    """
    title_name = models.CharField(max_length=100)
    text_field = models.TextField(max_length=50000)
    author_nick = models.ForeignKey('Author', on_delete=models.SET_NULL,
                                    null=True)
    post_date = models.DateTimeField(datetime.now(), auto_now_add=True, blank=False)

    objects = models.Manager()

    def __str__(self):
        """
        Representing post information
        """
        return '{0}'.format(self.title_name)

    def get_absolute_url_info(self):
        """
        Show detail information about post
        """
        return reverse('title-list', args=[str(self.id)])
