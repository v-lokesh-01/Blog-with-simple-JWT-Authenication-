from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title', 'content',]  # Include necessary fields
        read_only_fields = ['user', 'created_at']  # Prevent modification of user and created_at fields