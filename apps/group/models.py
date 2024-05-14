from django.db import models
from apps.divisi.models import Divisi
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model): 
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE, related_name='divisi_group')#sekretaris
    person = models.ManyToManyField(User, related_name='secretary_group')#orang orangnya
    type = models.IntegerField()
    