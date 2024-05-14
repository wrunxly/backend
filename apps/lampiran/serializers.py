from rest_framework import serializers
from .models import Lampiran

class LampiranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lampiran
        fields = ['id', 'nama_lampiran', 'file']

    def create(self, validated_data):
        return Lampiran.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('nama_lampiran', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance 