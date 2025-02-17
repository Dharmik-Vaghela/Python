from django.db import models

# Create your models here.
class Post(models.Model):
    post_heading = models.CharField(max_length=50)
    post_text = models.TextField()
    def __str__(self):
        return self.post_heading
    
class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)