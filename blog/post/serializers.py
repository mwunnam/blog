from .models import Post
from rest_framework import serializers
from comments.serializers import CommentSerializer 
from comments.models import Comment

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'created_at', 'comments_count', 'comments']