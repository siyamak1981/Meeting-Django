from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView,DetailView
from . models import TicketEnvelope,TicketLetter
from . forms import TicketEnvelopeForm, TicketLetterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.contrib import messages


class TicketsEnvelopeView(LoginRequiredMixin, ListView):
    template_name = "backend/ticket/list.html"
    context_object_name = 'ticket_list'
    paginate_by = 5
    def get_queryset(self):
        return TicketEnvelope.objects.all().select_related('user').order_by('-created')
    

class TicketCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = TicketEnvelope
    form_class = TicketEnvelopeForm
    template_name = 'backend/ticket/create.html'
    success_url = reverse_lazy('tickets:ticket_created_by_user')
    success_message = "Ticket Added Successfully!"

        
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["tickets"] = TicketLetter.objects.all()
    #     return context



class TicketEnvelopeByUserView(SuccessMessageMixin, LoginRequiredMixin, ListView):
    template_name = "backend/ticket/list_created_by_user.html"
    context_object_name = 'tickets'
    paginate_by = 5

    def get_queryset(self):
        return TicketEnvelope.objects.all().filter(user = self.request.user.id).select_related("user").order_by('-created')



@login_required
def ticketDetailView(request, *args, **kwargs):
    ticket = get_object_or_404(TicketEnvelope, pk = kwargs['pk'])
    ticket_envelops = TicketEnvelope.objects.prefetch_related('messages').filter(user = request.user.id).order_by('-created')[:5]

   
    if request.method == "POST":
        form = TicketLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ticket replay is created")
            return render(request, 'backend/ticket/list.html', {'form': form, 'ticket':ticket , 'ticket_envelops':ticket_envelops })
        else:
            messages.error(request, "error is accoure")
    else:
        form = TicketLetterForm()
    return render(request, 'backend/ticket/show.html', {'form': form , 'ticket':ticket, 'ticket_envelops':ticket_envelops })



class TicketsDoneView(ListView):
    template_name = "backend/ticket/show.html"
    context_object_name = 'ticket_list'
    def get_queryset(self):
        return TicketEnvelope.objects.all().select_related('user').filter(status = 'Done').order_by('-created')
