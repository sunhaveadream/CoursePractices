from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
	"""博客的字段定义"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""返回博客的标题"""
		return self.text

class BlogArtical(models.Model):
	"""博文的字段定义"""
	blogPost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
    
	class Meta:
		verbose_name_plural = 'blogarticales'
 
	def __str__(self):
		"""返回博文的内容"""
		return f"{self.text[:50]}..."
