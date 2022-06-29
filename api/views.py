from rest_framework import generics
from blog.models import Post
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from api.serializers import UserSerializer,PostSerializer,TagSerializer,CategorySerializer, SubCategorySerializer,ProfileSerializer
from tag.models import Tag
from category.models import Category, SubCategory
from users.models import Profile
from .permissions import (
	IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly,UserIsOwnerOrReadOnly,IsActiveOrReadOnly
)
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)
    

class APIProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsSuperUserOrStaffReadOnly]
        else:
            permission_classes = [IsActiveOrReadOnly, UserIsOwnerOrReadOnly,]
        return [permission() for permission in permission_classes]


class APIPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_fiels = "pk"
    lookup_url_kwarg = "pk"  
    filterset_fields = ['status','author__first_name']
    ordering_fields = ["status", "published_at"]
    ordering = ['-published_at']
    search_fields = ["title", "content", "author__first_name", "author__last_name"]
    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class APICategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_fiels = "pk"
    lookup_url_kwarg = "pk"  
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class APISubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_fiels = "pk"
    lookup_url_kwarg = "pk"  
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class APITagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_fiels = "pk"
    lookup_url_kwarg = "pk"
    permission_classes = (IsSuperUserOrStaffReadOnly,)







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