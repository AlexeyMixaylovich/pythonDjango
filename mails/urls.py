from django.urls import path

from mails.views import index
from mails.views import client
from mails.views import mailing
from mails.views import version


urlpatterns = [

     path('', index.IndexView.as_view(), name='index'),

     # Client   
     path('client/add/', client.ClientCreateView.as_view(), name='client-add'),
     path('client/delete/<int:pk>',
          client.ClientDeleteView.as_view(), name='client-delete'),
     path('client/<int:pk>/', client.ClientUpdateView.as_view(), name='client-update'),
     path('client/list/', client.ClientListView.as_view(), name='client-list'),

     # Mailing
     path('mailing/add/', mailing.MailingCreateView.as_view(), name='mailing-add'),
     path('mailing/delete/<int:pk>',
          mailing.VersionDeleteView.as_view(), name='mailing-delete'),
     path('mailing/<int:pk>/', mailing.MailingUpdateView.as_view(),
          name='mailing-update'),
     path('mailing/list/', mailing.MailingListView.as_view(), name='mailing-list'),


     # Version
     path('version/add/', version.VersionCreateView.as_view(), name='version-add'),
     path('version/delete/<int:pk>',
          version.VersionDeleteView.as_view(), name='version-delete'),
     path('version/<int:pk>/', version.VersionUpdateView.as_view(),
          name='version-update'),
     path('version/list/', version.VersionListView.as_view(), name='version-list'),



]
