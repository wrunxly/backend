from django.urls import include, path
from apps.jabatan.views import *

app_name = "jabatan"
urlpatterns = [
    path("", JabatanListCreateAPIView.as_view(), name="jabatan-list"),
    path("create/", JabatanListCreateAPIView.as_view(), name="jabatan-create"),
    path("details/<str:pk>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-detail"),
    path("update/<str:pk>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-update"),
    path("delete/<str:pk>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-delete"),
]