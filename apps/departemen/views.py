from rest_framework import generics
from apps.departemen.models import Departemen
from apps.departemen.serializers import DepartemenSerializer
from apps.profile.views.auth_views import IsAuthenticatedAndTokenExists

class DepartemenListCreateAPIView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedAndTokenExists]
    serializer_class = DepartemenSerializer

    def get_queryset(self):
        id_divisi = self.request.query_params.get('id_divisi')
        queryset = Departemen.objects.all()
        if id_divisi :
            queryset = queryset.filter(divisi_id = id_divisi)
        return queryset

class DepartemenRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Departemen.objects.all()
    serializer_class = DepartemenSerializer
    def get_queryset(self):
        id_divisi = self.request.query_params.get('id_divisi')
        queryset = Departemen.objects.all()
        if id_divisi :
            queryset = queryset.filter(divisi_id = id_divisi)
        return queryset
    # permission_classes = [IsAuthenticatedAndTokenExists]
