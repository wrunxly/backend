from django.urls import include, path
from apps.departemen.views import *

app_name = "departemen"
urlpatterns = [
    path("", DepartemenListCreateAPIView.as_view(), name="departemen-list"),
    path("create/", DepartemenListCreateAPIView.as_view(), name="departemen-create"),
    path("details/<str:pk>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-detail"),
    path("update/<str:pk>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-update"),
    path("delete/<str:pk>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-delete"),
]