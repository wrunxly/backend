from django.urls import include, path
from .views import *

app_name = "lampiran"
urlpatterns = [
    path("", LampiranListCreateView.as_view(), name="lampiran-list"),
    path("create/", LampiranListCreateView.as_view(), name="lampiran-create"),
    path("details/<int:pk>/", LampiranRetrieveUpdateDelete.as_view(), name="lampiran-detail"),
    path("update<int:pk>/", LampiranRetrieveUpdateDelete.as_view(), name="lampiran-update"),
    path("delete/<int:pk>/", LampiranRetrieveUpdateDelete.as_view(), name="lampiran-delete"),
]