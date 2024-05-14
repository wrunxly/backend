from rest_framework import serializers
from .models import Surat, Disposisi
from django.contrib.auth.models import User
from apps.profile.serializers.serializers_profile import UserSerializer
from apps.lampiran.serializers import LampiranSerializer

class LogSerializer(serializers.Serializer):
    aksi = serializers.CharField()
    oleh = serializers.CharField()
    tanggal = serializers.CharField()

class SuratSerializer(serializers.ModelSerializer):
    log = LogSerializer(many=True,required=False)
    # penerima = UserSerializer(many=True,read_only=True)
    penerima = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, write_only=True)
    penyetuju = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, write_only=True)
    lampiran_detail = LampiranSerializer(source='lampiran', read_only=True)
    penerima_detail = UserSerializer(source='penerima',many=True, read_only=True)
    penyetuju_detail = UserSerializer(source='penyetuju',many=True, read_only=True)


    class Meta:
        model = Surat
        fields = ['id','pembuat','penerima','penerima_detail','penyetuju','penyetuju_detail', 'no_agenda', 'no_surat', 'perihal', 'status', 'kategori', 'urgensi', 'tanggal_pengiriman','isi_surat','lampiran_detail','lampiran','file_surat', 'log']
        extra_kwargs = {'lampiran': {'write_only': True}}


    def create(self, validated_data):
        log_data = validated_data.pop('log', [])
        
        penerima_data = validated_data.pop('penerima', [])
        penyetuju_data = validated_data.pop('penyetuju', [])

        surat = Surat.objects.create(**validated_data)
        for data in log_data:
            surat.log.append(data)
            print(data)
        print(surat.log)
        for data in penerima_data:
            surat.penerima.add(data)
        for data in penyetuju_data:
            surat.penyetuju.add(data)
        surat.save()
        return surat

    def update(self, instance, validated_data):
        log_data = validated_data.pop('log', [])
        instance = super().update(instance, validated_data)
        for data in log_data:
            instance.log.append(data)
        return instance

class DisposisiSerializer(serializers.ModelSerializer):
    disposisi_oleh = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Disposisi 
        fields = ['id','disposisi_oleh','disposisi_kepada','surat', 'komentar', 'tanggal_disposisi']
    
    def create(self, validated_data):
        #user = self.context.get('user')
        disposisi = Disposisi.objects.create(disposisi_oleh = validated_data["disposisi_oleh"], surat = validated_data["surat"], komentar = validated_data["komentar"], 
                                        tanggal_disposisi = validated_data["tanggal_disposisi"])
        disposisi.save()

        for penerima in validated_data['disposisi_kepada']:
            disposisi.disposisi_kepada.add(penerima)

        return disposisi