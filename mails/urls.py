from django.urls import path

from mails.views import index
from mails.views import client
from mails.views import mailing
from mails.views import version



from . import views1

urlpatterns = [



    path('', index.IndexView.as_view(), name='index'),

    path('client/add/', client.ClientCreateView.as_view(), name='client-add'),
    path('client/delete/<int:pk>',
         client.ClientDeleteView.as_view(), name='client-delete'),
    path('client/<int:pk>/', client.ClientUpdateView.as_view(), name='client-update'),
    path('clients', client.ClientListView.as_view(), name='client-list'),




    path('mailing/add/', mailing.MailingCreateView.as_view(), name='mailing-add'),
    path('mailing/delete/<int:pk>',
         mailing.VersionDeleteView.as_view(), name='mailing-delete'),
    path('mailing/<int:pk>/', mailing.MailingUpdateView.as_view(),
         name='mailing-update'),
    path('mailings', mailing.MailingListView.as_view(), name='mailing-list'),



#     path('mailings/add-clients/<int:pk>',views1.MailingAddClients, name='mailing-add-clients'),
#     path('mailings/<int:pk>/add-client/<int:client_id>',views1.MailingAddClient, name='mailing-add-client'),
#     path('mailings/<int:pk>/del-client/<int:client_id>', views1.MailingDelClient, name='mailing-del-client'),



    path('version/add/', version.VersionCreateView.as_view(), name='version-add'),
    path('version/delete/<int:pk>',
         version.VersionDeleteView.as_view(), name='version-delete'),
    path('version/<int:pk>/', version.VersionUpdateView.as_view(),
         name='version-update'),
    path('versions', version.VersionListView.as_view(), name='version-list'),



]
