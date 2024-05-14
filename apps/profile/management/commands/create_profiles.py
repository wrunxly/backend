from django.core.management.base import BaseCommand
from apps.profile.models import Profile
from apps.departemen.models import Departemen
from apps.jabatan.models import Jabatan
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed profile data'

    def handle(self, *args, **kwargs):
        data_to_add = [
            {'user':19 ,'nama_lengkap': 'nadip abcd','alamat': 'Jl Tikus no 1','kota': 'Kota Bandung','phone_number': '081274712','nik_group': '52512','nik_lokal': '95827','organisasi': 'Telkom Indonesia','is_first_login': True,'departemen': 12,'jabatan': 1},
            {'user':20 ,'nama_lengkap': 'nopal alga','alamat': 'Jl Kelinci no 2','kota': 'Kota Padang','phone_number': '081277264','nik_group': '56274','nik_lokal': '67242','organisasi': 'Pertamina','is_first_login': True,'departemen': 13,'jabatan': 2},
            {'user':21 ,'nama_lengkap': 'jalu kawani','alamat': 'Jl Harimau no 3','kota': 'Kab. Ciwidey','phone_number': '081270285','nik_group': '12631','nik_lokal': '19582','organisasi': 'PT POS Indonesia','is_first_login': True,'departemen': 14,'jabatan': 3},
        ]
        for data in data_to_add:
            user = data.get('user')
            nama_lengkap = data.get('nama_lengkap')
            alamat = data.get('alamat')
            kota = data.get('kota')
            phone_number = data.get('phone_number')
            nik_group = data.get('nik_group')
            nik_lokal = data.get('nik_lokal')
            organisasi = data.get('organisasi')
            is_first_login = data.get('is_first_login')
            departemen = data.get('departemen')
            jabatan = data.get('jabatan')

            user_obj = User.objects.get(id=user)
            departemen_obj = Departemen.objects.get(id=departemen)
            jabatan_obj = Jabatan.objects.get(id=jabatan)

            profile = Profile.objects.create(user=user_obj, nama_lengkap=nama_lengkap, alamat=alamat, kota=kota, phone_number=phone_number, nik_group=nik_group, nik_lokal=nik_lokal, organisasi=organisasi, is_first_login=is_first_login, departemen=departemen_obj, jabatan=jabatan_obj)

            self.stdout.write(self.style.SUCCESS(f"Profile '{nama_lengkap}' berhasil ditambahkan"))