from rest_framework import serializers
from api.blog.models import Blog


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model =Blog
        fields =('title','description','category','created_at')