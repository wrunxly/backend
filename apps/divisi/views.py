from rest_framework import generics
from apps.divisi.models import Divisi
from apps.divisi.serializers import DivisiSerializer
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists

class DivisiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer
    # permission_classes = [IsAuthenticatedAndTokenExists]

class DivisiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer
    # permission_classes = [IsAuthenticatedAndTokenExists]
    # lookup_field = 'id_divisi'
