from rest_framework import generics
from apps.jabatan.models import Jabatan
from apps.jabatan.serializers import JabatanSerializer
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists

class JabatanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer
    permission_classes = [IsAuthenticatedAndTokenExists]

class JabatanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer
    permission_classes = [IsAuthenticatedAndTokenExists]
    # lookup_field = 'id_jabatan'
