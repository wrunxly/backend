from rest_framework import generics
from apps.profile.models import *
from apps.profile.serializers.serializers_profile import *
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists
from rest_framework.response import Response
from django.contrib.auth.models import User


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        id_user = self.request.query_params.get('id_user')
        id_jabatan = self.request.query_params.get('id_jabatan')
        id_departemen = self.request.query_params.get('id_departemen')
        queryset = Profile.objects.all()
        if id_user :
            queryset = queryset.filter(user_id = id_user)
        elif id_departemen :
            queryset = queryset.filter(departemen_id = id_departemen)
        elif id_jabatan :
            queryset = queryset.filter(jabatan_id = id_jabatan)
        return queryset
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfileUpdateRetrieveAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'user_id'
    
    def get_queryset(self):
        id = self.kwargs[self.lookup_field]
        queryset = Profile.objects.filter(user_id = id)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True, context={'request': request}) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
class SekretarisListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SekretarisSerializer

    def get_queryset(self):
        id_user = self.request.query_params.get('id_user')
        profile = Profile.objects.get(user_id=id_user)
        queryset = Sekretaris.objects.all()
        if profile :
            queryset = queryset.filter(atasan_id = profile.id)
        return queryset
    
    def post(self, request):
        serializer = SekretarisSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class SekretarisUpdateRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SekretarisSerializer
    queryset = Sekretaris.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DelegasiListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DelegasiSerializer

    def get_queryset(self):
        id_user = self.request.query_params.get('id_user')
        profile = Profile.objects.get(user_id=id_user)
        queryset = Delegasi.objects.all()
        if profile :
            queryset = queryset.filter(atasan_id = profile.id)
        return queryset
    
    def post(self, request):
        serializer = DelegasiSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DelegasiUpdateRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DelegasiSerializer
    queryset = Delegasi.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)