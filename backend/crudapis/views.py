from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class BlogList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        # Only allow users to access their own blogs
        return Blog.objects.filter(user=self.request.user)





class BlogCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


    def perform_create(self, serializer):
        # Ensure that the user is set when creating a blog post
        serializer.save(user=self.request.user)


class BlogDelete(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer  
    
    def get_queryset(self):
        # Only allow users to access their own blogs
        return Blog.objects.filter(user=self.request.user)

    

    