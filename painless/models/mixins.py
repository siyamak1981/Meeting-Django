from django.db import models
from painless.models.choices import PostStatus


status = PostStatus(is_charfield=False)


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrganizedMixin(TimeStampedMixin):
    title = models.CharField(
        max_length=128, unique_for_month='created', help_text='must be unique')
    slug = models.CharField(max_length=128, unique_for_month='created',)
    status = models.PositiveSmallIntegerField(
        choices=status.get_status(), default=status.DRAFT)

    class Meta:
        abstract = True
