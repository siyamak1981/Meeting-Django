from django.contrib import admin
from . import models
from painless.models.actions import PostableMixin
from painless.models.actions import ExportMixin
from khayyam import JalaliDate as jd




@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    list_display = ['title', 'slug', 'is_published', 'published', 'subcategory', 'get_tags']
    list_editable = ['subcategory']
    filter_horizontal = ['tag']
    list_filter = ['status', 'published_at', 'subcategory__title']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
  
    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title',), 
                    ('author', 'status', ),
                    'subcategory'
                     
                ),
            }
        ),

        ('Advanced_options', { 
            'fields': (
                    'tag',
                    'banner',
                    'summary',
                    'content',
                    'published_at',
                ),
            'classes': ('collapse',)
            },

        ),
    ]

    def published(self, obj):
        return jd(obj.published_at)

    def get_tags(self, obj):
        return ", ".join([t.title for t in obj.tag.all()])

    def is_published(self, obj):
        published = 1
        return obj.status == published
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []

    is_published.boolean = True


admin.site.site_header = "Siyamak Adminstration"
admin.site.site_title = "Siyamak site admin"
admin.site.index_title = "Welcome to Siyamak dashboard"

