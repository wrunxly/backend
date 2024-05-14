from django.urls import include, path
from .views import *

app_name = "surat"
urlpatterns = [ 
    path("", SuratListCreateView.as_view(), name="surat-list"),
    path("create/", SuratListCreateView.as_view(), name="surat-create"),
    path("details/<int:pk>/", SuratRetrieveUpdateDelete.as_view(), name="surat-detail"),
    path("update/<int:pk>/", SuratRetrieveUpdateDelete.as_view(), name="surat-update"),
    path("delete/<int:pk>/", SuratRetrieveUpdateDelete.as_view(), name="surat-delete"),
    path("disposisi/", DisposisiListCreateView.as_view(), name="disposisi-list"),
    path("disposisi/create/", DisposisiListCreateView.as_view(), name="disposisi-create"),
    path("disposisi/details/<int:pk>/", DisposisiRetrieve.as_view(), name="surat-detail"),
]