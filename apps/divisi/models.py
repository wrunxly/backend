from django.db import models

class Divisi(models.Model):
    nama_divisi = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    kode_divisi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_divisi
