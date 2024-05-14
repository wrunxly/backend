from django.core.management.base import BaseCommand
from apps.divisi.models import Divisi
from apps.divisi.serializers import DivisiSerializer

class Command(BaseCommand):
    help = 'Seed divisi data'

    def handle(self, *args, **kwargs):
        data_to_add = [
            {'nama_divisi': 'IT'},
            {'nama_divisi': 'HR'},
            {'nama_divisi': 'PR'},
        ]

        serializer = DivisiSerializer(data=data_to_add, many=True)
        if serializer.is_valid():
            Divisi.objects.bulk_create([Divisi(**item) for item in serializer.validated_data])
            self.stdout.write(self.style.SUCCESS('Data Divisi berhasil ditambahkan secara massal.'))
        else:
            self.stdout.write(self.style.ERROR(f"Error: {serializer.errors}"))