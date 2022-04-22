from django import forms
from . models import TicketLetter,TicketEnvelope


class TicketEnvelopeForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))
    class Meta:
        model = TicketEnvelope
        exclude = ('published_at',)


class TicketLetterForm(forms.ModelForm):
    class Meta:
        model = TicketLetter
        exclude = ('published_at',)