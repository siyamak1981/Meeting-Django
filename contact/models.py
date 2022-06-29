import uuid
from django.db import models
from painless.models.mixins import TimeStampedMixin



class Contact(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    subject = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created', 'subject']
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        get_latest_by = ['-created']

    def __str__(self):
        return self.subject

