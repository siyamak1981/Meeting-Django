from django.db import models
from painless.models.choices import PostStatus
from django.utils import timezone


status = PostStatus(is_charfield=False)


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        abstract = True


class OrganizedMixin(TimeStampedMixin):
    title = models.CharField(
        max_length=128, unique_for_month='published_at', help_text='must be unique')
    slug = models.CharField(max_length=128, unique_for_month='published_at',)
    status = models.PositiveSmallIntegerField(
        choices=status.get_status(), default=status.DRAFT)

    class Meta:
        abstract = True
