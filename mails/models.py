from django.db import models
from django.urls import reverse


class Client(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=500)

  def __str__(self):
    return self.name+ ' ' + self.name
  def get_absolute_url(self):
    return reverse('client-list')

class Mailing(models.Model):
  name = models.CharField(max_length=200)
  version = models.ForeignKey('Version', on_delete=models.DO_NOTHING, null=True)
  clients = models.ManyToManyField(Client)

  
  def get_absolute_url(self):
    return reverse('mailing-list')

class Version(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=500)

  def __str__(self):
    return 'Версия ' + self.name

  def get_absolute_url(self):
    return reverse('version-list')
