from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'), ('published', 'Published'))
    YES_NO_CHOICE = (('yes', 'Yes'), ('no', 'No'))
    title = models.CharField(max_length=125)
    header_image = models.ImageField(upload_to='images/', default='default.jpg')
    slug = models.CharField(null=True, blank=True, max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_category")
    trending = models.CharField(max_length=5, choices=YES_NO_CHOICE, default="no")
    editors_pick = models.CharField(max_length=5, choices=YES_NO_CHOICE, default="no")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="draft")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']

    def get_absolute_url(self):
        return reverse('single_post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug
                             ])
