from django.db import models

# Create your models here.
class Lampiran(models.Model):
    nama_lampiran = models.CharField(max_length=100)
    file = models.FileField(upload_to='event_files/')

    def __str__(self):
        return self.nama_lampiran 