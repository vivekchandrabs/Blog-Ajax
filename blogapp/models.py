from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(default=None)
	timestamp = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title

	def natural_key(self):
		return {"id":self.pk, "title":self.title, "content":self.content}
