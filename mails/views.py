from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.views import generic

# from .forms import ClientForm

from .models import Client, Mailing, ClientsToMailing




class IndexView(generic.TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['pidor'] = 'ПИДОР'
    return context


class ClientListView(generic.ListView):
  model = Client

class ClientCreateView(CreateView):
  model = Client
  fields = ('name', 'email')


class ClientUpdateView(UpdateView):
  model = Client
  fields = ('name', 'email')


class MailingListView(generic.ListView):
  model = Mailing


class MailingCreateView(CreateView):
  model = Mailing
  fields = ['name']


class MailingUpdateView(UpdateView):
  model = Mailing
  fields = ['name']




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


# def MailingAddClient(request, pk):
#     # book_inst = get_object_or_404(Mailing, pk=pk)

#     # Если данный запрос типа POST, тогда
#     if request.method == 'POST':

#         # Создаём экземпляр формы и заполняем данными из запроса (связывание, binding):
#         form = RenewBookForm(request.POST)

#         # Проверка валидности данных формы:
#         if form.is_valid():
#             # Обработка данных из form.cleaned_data
#             #(здесь мы просто присваиваем их полю due_back)
#             book_inst.due_back = form.cleaned_data['renewal_date']
#             book_inst.save()

#             # Переход по адресу 'all-borrowed':
#             return HttpResponseRedirect(reverse('all-borrowed') )

#     # Если это GET (или какой-либо ещё), создать форму по умолчанию.
#     else:
#         proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#         form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

#     return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})