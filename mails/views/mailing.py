from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from mails.models import Mailing

class MailingListView(ListView):
  extra_context = {'active': 'mailing'}
  model = Mailing

  def get_queryset(self):
      return Mailing.objects.all().select_related('version')


class MailingCreateView(CreateView):
  extra_context = {'active': 'mailing'}
  model = Mailing
  fields = ['name', 'version', 'clients']


class MailingUpdateView(UpdateView):
  extra_context = {'active': 'mailing'}
  model = Mailing
  fields = ['name', 'version', 'clients']


class VersionDeleteView(DeleteView):
  extra_context = {'active': 'client'}
  model = Mailing
  success_url = reverse_lazy('mailing-list')
