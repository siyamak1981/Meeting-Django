from django.urls import re_path, include
from rest_framework import routers 
from blog.models import Post
from api.views import UserViewSet,\
APITagViewSet,APIPostViewSet, APICategoryViewSet, APISubCategoryViewSet,APIProfileViewSet
from dj_rest_auth.views import PasswordResetConfirmView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tags', APITagViewSet)
router.register(r'posts', APIPostViewSet)
router.register(r'categories', APICategoryViewSet)
router.register(r'subcategories', APISubCategoryViewSet)
router.register(r'profile', APIProfileViewSet)



urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('dj_rest_auth.registration.urls'))
    re_path(r'^v1/rest-auth/password/reset/confirm/<uuid>/<token>/', PasswordResetConfirmView.as_view(), name = "password-reset-confirm")

    # re_path(r'^posts/',APIPostListCreateView.as_view(), name = "list"),
    # re_path(r'^post/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12})/$', APIPostDetailView.as_view(), name = 'detail'),
    # re_path(r'^post/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12})/edit/$', APIPostUpdateDestroyDetailView.as_view(), name = 'edit'),
    # re_path(r'^tags/', APITagListCreateView.as_view(), name = 'list'),
    # re_path(r'^tag/(?P<pk>[-\d]+)/', APITagDetailView.as_view(), name = 'detail'),
    # re_path(r'^tag/(?P<pk>[-\d]+)/edit/$', APITagEditView.as_view(), name = 'edit'),
    
]
