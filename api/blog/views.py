from rest_framework import generics
from api.blog import serializers
from api.blog.models import Blog

# Create your views here.

class ListBlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogListSerializer

class DetailBlogAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogListSerializer

class CreateBlogAPIView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogListSerializer
    
class UpdateBlogAPIView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogListSerializer
    