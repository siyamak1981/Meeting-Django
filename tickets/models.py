import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from painless.models.mixins import TimeStampedMixin
from django.contrib.auth import get_user_model
User = get_user_model()


class TicketLetter(TimeStampedMixin):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title= models.CharField(_('title'),max_length=128)
    description = models.TextField(max_length=1000,verbose_name=_('Message'))
    user = models.ForeignKey(User, on_delete = models.SET_NULL, related_name="ticket_letter_user", null = True , blank = True)
    reply = models.ForeignKey('TicketEnvelope', on_delete = models.CASCADE, blank =True, null = True, related_name='letter_reply', verbose_name=_('Reply'))
    ticket = models.ForeignKey('TicketEnvelope', on_delete = models.CASCADE, related_name='messages', verbose_name = _('Ticket'), blank = True, null = True)
    
    class Meta:
        verbose_name = _('TicketLetters')
        verbose_name_plural = _('TicketLetters')
        ordering = ['-created']
    
    def __str__(self):
        return "{}".format(self.user)

    def get_absolute_url(self):
        return reverse('tickets:detail', kwargs={"pk": self.pk})


class Department(TimeStampedMixin): #1 to many
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank = True, null = True)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
    

    def __str__(self):
        return self.title
   


class TicketEnvelope(TimeStampedMixin):

    PRIORITY_CHOICES = (
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
        ('Critical','Critical'),
    )
    STATUS_CHOICES = (
        ('Backlog','Backlog'),
        ('Waiting On Submitter','Waiting On Submitter'),
        ('Progress','Progress'),
        ('Done','Done'),
    )
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    subject = models.CharField(max_length=128)
    department = models.ForeignKey("Department", on_delete=models.CASCADE ,related_name="ticket")
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES, blank=True)
    description = models.TextField(max_length=1000, verbose_name=_('Message'))
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, blank = True, null = True, related_name='ticket_envelop_user', verbose_name=_('Ticket to'))
    
    class Meta:
        verbose_name = _('TicketEnvelop')
        verbose_name_plural = _('TicketsEnvelops')
        ordering = ['-created']

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return reverse('tickets:detail', kwargs={"pk": self.pk})


class Attachment(models.Model): #1 to many
    title = models.CharField(max_length=128)
    attachment= models.FileField(upload_to='tickets', 
                                        validators = [FileExtensionValidator(['docx', 'doc', 'pdf', 'png', 'gepg','jpg'])],
                                        help_text = "supported file: doc, pdf, jpg, png and docx")
    ticket = models.ForeignKey("TicketEnvelope", on_delete = models.CASCADE, related_name="attachments")

    class Meta:
        verbose_name = "attachment"
        verbose_name_plural = "attachments"
    
    def __str__(self):
        return self.title