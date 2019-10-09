from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(default=None)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def natural_key(self):
		return {"id":self.pk, "title":self.title, "content":self.content}

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	content = models.TextField(default=None)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.post} | {self.content}"