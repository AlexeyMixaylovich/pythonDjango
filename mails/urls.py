from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('client/add/', views.ClientCreateView.as_view(), name='client-add'),
    path('client/<int:pk>/', views.ClientUpdateView.as_view(), name='client-update'),
    path('clients', views.ClientListView.as_view(), name='client-list'),
    path('mailing/add/', views.MailingCreateView.as_view(), name='mailing-add'),
    path('mailing/<int:pk>/', views.MailingUpdateView.as_view(), name='mailing-update'),
    path('mailings', views.MailingListView.as_view(), name='mailing-list'),
    path('mailings/add-clients/<int:pk>',views.MailingAddClients, name='mailing-add-clients'),
    path('mailings/<int:pk>/add-client/<int:client_id>',views.MailingAddClient, name='mailing-add-client'),
    path('mailings/<int:pk>/del-client/<int:client_id>', views.MailingDelClient, name='mailing-del-client'),



]
