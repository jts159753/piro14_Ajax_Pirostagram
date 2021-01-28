from django.db import models
from ajax.utils import uuid_upload_to

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image=models.ImageField(upload_to=uuid_upload_to)
    like = models.BooleanField(default=False)

class Comment(models.Model):
    content=models.TextField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")