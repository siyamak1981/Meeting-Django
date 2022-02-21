
from django.contrib import admin
from django.urls import re_path, include
from insurance import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    re_path(r'^api/', include('api.urls')),
    re_path(r'^', include('accounts.urls',namespace='accounts')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^dashboard/', include('dashboard.urls')),
    re_path(r'^tag/', include('tag.urls')),
    re_path(r'^category/', include('category.urls')),
    re_path(r'^contact/', include('contact.urls')),
    re_path(r'^user/', include('users.urls')),
    re_path(r'^', include('frontend.urls',namespace='frontend')),
    re_path(r'^subcategory/', include('category.subcaturls')),
    re_path(r'^social-auth/', include('social_django.urls', namespace='social')),
    re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^__debug__/', include('debug_toolbar.urls')),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='backend/accounts/login.html'), name='login'),
    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^accounts/reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='backend/accounts/password_reset.html',
            html_email_template_name='backend/accounts/password_reset_email.html',
            email_template_name='backend/accounts/password_reset_email.html',
            subject_template_name='backend/accounts/password_reset_subject.txt'
        ),
        name='password_reset'),
    re_path(r'^accounts/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='backend/accounts/password_reset_done.html'),
        name='password_reset_done'),
    re_path(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='backend/accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    re_path(r'^accounts/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='backend/accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    re_path(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='backend/accounts/password_change_done.html'),
        name='password_change_done'),
    re_path(r'^.*\.*', views.pages, name='pages'),
    
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)