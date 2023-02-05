from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy


from mails.models import Client


class ClientListView(ListView):
  extra_context = {'active': 'client'}
  model = Client


class ClientCreateView(CreateView):
  extra_context = {'active': 'client'}
  model = Client
  fields = ('name', 'email')


class ClientUpdateView(UpdateView):
  extra_context = {'active': 'client'}
  model = Client
  fields = ('name', 'email')


class ClientDeleteView(DeleteView):
  extra_context = {'active': 'client'}
  model = Client
  success_url = reverse_lazy('client-list')
