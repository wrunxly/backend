from django.urls import include, path
from apps.divisi.views import *

app_name = "divisi"
urlpatterns = [
    path("", DivisiListCreateAPIView.as_view(), name="divisi-list"),
    path("create/", DivisiListCreateAPIView.as_view(), name="divisi-create"),
    path("details/<str:pk>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-detail"),
    path("update/<str:pk>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-update"),
    path("delete/<str:pk>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-delete"),
]