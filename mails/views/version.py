from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from mails.models import Version


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
