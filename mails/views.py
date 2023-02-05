from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView

# from .forms import ClientForm

from .models import Client, Mailing, ClientsToMailing, Version




class IndexView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['pidor'] = 'ПИДОР'
    return context


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

class MailingListView(ListView):
  extra_context = {'active': 'mailing'}
  # queryset = Book.objects.filter(publisher__name='ACME Publishing')
  model = Mailing

  def get_queryset(self):
      return Mailing.objects.all().select_related('version')

class MailingCreateView(CreateView):
  extra_context = {'active': 'mailing'}
  model = Mailing
  fields = ['name', 'version']

class MailingUpdateView(UpdateView):
  extra_context = {'active': 'mailing'}
  model = Mailing
  fields = ['name', 'version']

def MailingAddClients(request, pk):

  clients_to_mailing = {}
  for client in ClientsToMailing.objects.all().filter(mailing=pk):
    clients_to_mailing[client.client] = client.mailing

  clients = []
  for client in Client.objects.all():
    if clients_to_mailing.get(client.id):
      is_add = True
    else:
      is_add = False
    clients.append({ 'id': client.id, 'name': client.name, 'email': client.email, 'is_add': is_add})

  context = {
      'mailing': Mailing.objects.get(id=pk),
      'client_list': clients,
  }
  return render(request, 'mails/mailing_add_client_list.html', context)


def MailingAddClient(request, pk, client_id):
  if not ClientsToMailing.objects.all().filter(mailing=pk, client=client_id).exists():
    newRecord = ClientsToMailing(mailing=pk, client=client_id)
    newRecord.save()

  return redirect('mailing-add-clients', pk)


def MailingDelClient(request, pk, client_id):
  ClientsToMailing.objects.filter(mailing=pk, client=client_id).delete()
  return redirect('mailing-add-clients', pk)


def ClientDelete(request, pk):
  Client.objects.filter(id=pk).delete()
  ClientsToMailing.objects.filter(client=pk).delete()

  return redirect('client-list')

def MailingDelete(request, pk):
  Mailing.objects.filter(id=pk).delete()
  ClientsToMailing.objects.filter(mailing=pk).delete()

  return redirect('mailing-list')


class VersionCreateView(CreateView):
  extra_context = {'active': 'version'}
  model = Version
  fields = ('name', 'description')


class VersionUpdateView(UpdateView):
  extra_context = {'active': 'version'}
  model = Version
  fields = ('name', 'description')


class VersionListView(ListView):
  extra_context = {'active': 'version'}
  model = Version


class VersionDeleteView(DeleteView):
  extra_context = {'active': 'version'}
  model = Version
  success_url = reverse_lazy('version-list')
