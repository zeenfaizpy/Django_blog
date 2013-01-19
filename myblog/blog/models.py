from django.db import models
from django.forms import ModelForm

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title



class Comment(models.Model):
	author = models.CharField(max_length=60)
	subject = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post)

	def __unicode__(self):
		return self.subject

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ["post"]



