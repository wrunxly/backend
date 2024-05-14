from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Lampiran
from .serializers import LampiranSerializer

class LampiranListCreateView(generics.ListCreateAPIView):
    queryset = Lampiran.objects.all()  # Specify queryset for the view
    serializer_class = LampiranSerializer  # Specify serializer class for the view

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    serializer_class = LampiranSerializer
    def get(self, request):
        lampirans = Lampiran.objects.all()
        serializer = LampiranSerializer(lampirans, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class LampiranRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lampiran.objects.all()
    serializer_class = LampiranSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)