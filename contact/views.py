
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls.base import  reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from contact.models import Contact
from contact.forms import ContactForm
from contact.tasks import my_first_task



class ListContactView(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'backend/contact/list.html'
    paginate_by = 10

    # it is for pagination
    def get_queryset(self):
        filter_val = self.request.GET.get("filter", "")
        order_by = self.request.GET.get("orderby", "pk")
        if filter_val != "":
            contact = Contact.objects.filter(Q(title__contains=filter_val) | Q(
                description__contains=filter_val)).order_by(order_by)
        else:
            contact = Contact.objects.all().order_by(order_by)

        return contact

    def get_context_data(self, **kwargs):
        context = super(ListContactView, self).get_context_data(**kwargs)
        context["filter"] = self.request.GET.get("filter", "")
        context["orderby"] = self.request.GET.get("orderby", "pk")
        context["all_table_fields"] = Contact._meta.get_fields()
        return context


class CreateContactView(SuccessMessageMixin , CreateView):
    model = Contact
    page_name = "contact"
    template_name = 'frontend/contact/create.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:create')
    success_message = "Contact Create successfully"
    def post(self, request, *args, **kwargs):
            if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    my_first_task.delay(2)
                    form.save()
                    messages.success(request,
                                    "Tank you for contact us!")
                    return redirect("contact:create")
            else:
                form = ContactForm()
            return render(request, 'frontend/contact/create.html',
                        {'form': form, },
                        )


class DeleteContactView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Contact
    permission_required = "contact.delete_contact"
    template_name = 'backend/contact/list.html'
    success_url = reverse_lazy('contact:list')
    success_message = "Contact Delete successfully"


    def handle_no_permission(self):
        messages.warning(self.request, "You dont have permission to this page please signin with superuser!")
        return redirect("dashboard:home")

    def get(self, request, *args, **kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            Contact_object = Contact.objects.get_queryset().filter(pk= pk)
            if Contact_object is not None:
                Contact_object.delete()
                messages.success(request, 'Contact was deleted.') 
                return redirect('contact:list')
        return redirect('backend/Contact/list.html')
       


class ContactShowView(SuccessMessageMixin,PermissionRequiredMixin, UpdateView):
    permission_required = "contact.update_contact"
    model = Contact
    template_name = 'backend/contact/show.html'
    fields = "__all__" 
    success_url = reverse_lazy('contact:list')
    
    def handle_no_permission(self):
        messages.warning(self.request, "You dont have permission to this page please signin with superuser!")
        return redirect("dashboard:home")

