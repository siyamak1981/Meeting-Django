from rest_framework import generics
from blog.models import Post
from rest_framework import routers, serializers, viewsets
from accounts.models import User
from api.serializers import UserSerializer,PostSerializer,TagSerializer,CategorySerializer, SubCategorySerializer,ProfileSerializer
from tag.models import Tag
from category.models import Category, SubCategory
from users.models import Profile

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class APIProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class APIPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_fiels = "pk"
    lookup_url_kwarg = "pk"  


class APICategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_fiels = "pk"
    lookup_url_kwarg = "pk"  

class APISubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_fiels = "pk"
    lookup_url_kwarg = "pk"  


class APITagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_fiels = "pk"
    lookup_url_kwarg = "pk"









# class APIPostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

    
# class APIPostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
#     lookup_fiels = "pk"
#     lookup_url_kwarg = "pk"    


# class APIPostUpdateDestroyDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
#     lookup_fiels = "pk"
#     lookup_url_kwarg = "pk"