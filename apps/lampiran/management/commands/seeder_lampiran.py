from django.core.management.base import BaseCommand
from apps.lampiran.models import Lampiran
from apps.lampiran.serializers import LampiranSerializer

class Command(BaseCommand):
    help = 'Seed divisi data'

    def handle(self, *args, **kwargs):
        data_to_add = [
            {'nama_lampiran': 'Surat Undangan', 'file':r'C:\Users\anbur\ARM\Coofis NDE v2.1.pdf'},
            {'nama_lampiran': 'Surat Keterangan', 'file':r'C:\Users\anbur\ARM\Coofis NDE v2.1.pdf'},
            {'nama_lampiran': 'Surat Izin', 'file':r'C:\Users\anbur\ARM\Coofis NDE v2.1.pdf'},
        ]

        serializer = LampiranSerializer(data=data_to_add, many=True)
        if serializer.is_valid():
            lampiran_instances = []
            for item in serializer.validated_data:
                nama_lampiran = item.get('nama_lampiran')
                file_path = item.get('file')
                print(f"File path: {file_path}")
                # Baca file dari path
                with open(file_path, 'rb') as file:
                    # Buat instance Lampiran dan simpan file
                    lampiran = Lampiran(nama_lampiran=nama_lampiran)
                    lampiran.file.save(file.name, file, save=True)  # Simpan file dengan nama aslinya
                    lampiran_instances.append(lampiran)

            Lampiran.objects.bulk_create(lampiran_instances)
            self.stdout.write(self.style.SUCCESS('Data Lampiran berhasil ditambahkan secara massal.'))
        else:
            self.stdout.write(self.style.ERROR(f"Error: {serializer.errors}"))