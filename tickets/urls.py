from django.urls import path, re_path
from . import views

app_name = 'tickets'

urlpatterns = [
    re_path(r'^list/', views.TicketsEnvelopeView.as_view(), name='list'),
    re_path(r'^create/', views.TicketCreateView.as_view(), name='create'),
    re_path(r'^created_by/', views.TicketEnvelopeByUserView.as_view(), name='ticket_created_by_user'),
    re_path(r'^done/$', views.TicketsDoneView.as_view(), name='ticket_done_queue'),
    re_path(r'^(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12})/detail', views.ticketDetailView, name='detail'),
]
