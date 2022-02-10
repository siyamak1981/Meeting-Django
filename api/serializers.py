from rest_framework import serializers
from blog.models import Post
from tag.models import Tag
from category.models import Category, SubCategory
from accounts.models import User
from users.models import Profile
from category.models import Category, SubCategory


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'is_superuser']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'pk', 'user', 'avatar', 'birthday', 'gender', 'phone', 'number', 'city', 'zip']


class TagSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Tag
            fields = ["url", "pk", "title", 'status', "created", "updated"]



class CategorySerializer(serializers.HyperlinkedModelSerializer):
       
        class Meta:
            model = Category
            fields = ["url", "pk", "title", "content", "banner", "created", "updated"]

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = SubCategory
            fields = ["url", "pk", "title", "content", "banner", "category"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["url", "pk", "title", "status", "summary", "banner", "content", "author", "created", "updated", "published_at","subcategory", "tag"]
        

# class PostDetailSerializer(serializers.ModelSerializer):
#     subcategory = SubCategorySerializer(required = True)
#     author = UserSerializer(required = True)
#     tag = TagSerializer(many = True, required = True)
#     class Meta:
#         model = Post
#         fields = ["pk","title", "status", "summary", "banner", "content", "author", "created", "updated", "published_at","tag","subcategory"]