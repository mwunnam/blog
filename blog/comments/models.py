from django.db import models
from post.models import Post
from user.models import User

class Comment(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    post   = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Comment by {self.author} at {self.created_at}'