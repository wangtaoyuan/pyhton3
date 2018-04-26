from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
	title = models.CharField(max_length=300)#charField类型，字段最大数量300
	author = models.ForeignKey(User, related_name="blog_posts")#foreingnKey表示允许一对多
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	
	class Meta:
		ordering = ("-publish",)
		
	def __str__(self):
		return self.title