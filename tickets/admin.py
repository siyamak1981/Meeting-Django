from django.contrib import admin
from . models import  Attachment, TicketLetter, Department, TicketEnvelope
from painless.models.actions import PostableMixin
from painless.models.actions import ExportMixin
from . import models


class AttachmentInline(admin.StackedInline):
    model = models.Attachment
    fields = [
        ('title','attachment',),
    ]


@admin.register(models.TicketEnvelope)
class TicketEnvelopeAdmin(admin.ModelAdmin, ExportMixin):
    list_display = ['department', 'subject', 'priority', 'created', 'status']
    inlines = [AttachmentInline]
    list_editable = ['status']
    list_filter = ['priority']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
 


@admin.register(models.TicketLetter)
class TicketLetterAdmin(admin.ModelAdmin, ExportMixin):
    list_display = ['title', 'user', 'ticket']
    list_filter = ['ticket']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
 


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin, ExportMixin):
    list_display = ['title']
    list_filter = ['title']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']



