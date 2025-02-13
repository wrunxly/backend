# Generated by Django 4.1.13 on 2024-05-08 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("lampiran", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Surat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("no_agenda", models.CharField(max_length=100)),
                ("no_surat", models.CharField(max_length=100)),
                ("perihal", models.CharField(max_length=100)),
                ("kategori", models.CharField(max_length=100)),
                ("urgensi", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("tanggal_pengiriman", models.DateField()),
                ("jenis_surat", models.CharField(max_length=100)),
                ("prioritas_surat", models.CharField(max_length=100)),
                ("komentar_surat", models.JSONField(default=list)),
                ("isi_surat", models.TextField(default="-")),
                ("log", models.JSONField(default=list)),
                ("file_surat", models.FileField(upload_to="event_files/")),
                (
                    "lampiran",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lampiran_surat",
                        to="lampiran.lampiran",
                    ),
                ),
                (
                    "pembuat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pembuat_surat",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "penerima",
                    models.ManyToManyField(
                        related_name="penerima_surat", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "penyetuju",
                    models.ManyToManyField(
                        related_name="penyetuju_surat", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "referensi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="referensi_surat",
                        to="lampiran.lampiran",
                    ),
                ),
                (
                    "tembusan",
                    models.ManyToManyField(
                        related_name="tembusan_surat", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Disposisi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("komentar", models.CharField(max_length=100)),
                ("tanggal_disposisi", models.DateField()),
                (
                    "disposisi_kepada",
                    models.ManyToManyField(
                        related_name="disposisi_kepada", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "disposisi_oleh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="disposisi_oleh",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "surat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="surat",
                        to="surat.surat",
                    ),
                ),
            ],
        ),
    ]
