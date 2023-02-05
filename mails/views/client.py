from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View, ListView
from django.urls import reverse_lazy


from mails.models import Client


class BaseClient(View):
  model = Client
  extra_context = {'active': 'client'}


class BaseEditClient(BaseClient):
  fields = ('name', 'email')
  success_url = reverse_lazy('client-list')



class ClientListView(BaseClient, ListView):
  pass


class ClientCreateView(BaseEditClient, CreateView):
  pass


class ClientUpdateView(BaseEditClient, UpdateView):
  pass


class ClientDeleteView(BaseEditClient, DeleteView):
  pass
