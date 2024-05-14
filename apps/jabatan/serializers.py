from rest_framework import serializers
from apps.jabatan.models import Jabatan

class JabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jabatan
        fields = ['id', 'nama_jabatan']

    def create(self, validated_data):
        return Jabatan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nama_jabatan = validated_data.get('nama_jabatan', instance.nama_jabatan)
        instance.save()
        return instance
