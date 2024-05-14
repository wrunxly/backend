from django.urls import include, path
from .views import *

app_name = "group"
urlpatterns = [ 
    path("", GroupListCreateView.as_view(), name="group-list"),
    path("create/", GroupListCreateView.as_view(), name="group-create"),
    path("details/<int:pk>/", GroupRetrieveUpdateDelete.as_view(), name="group-detail"),
    path("update/<int:pk>/", GroupRetrieveUpdateDelete.as_view(), name="group-update"),
    path("delete/<int:pk>/", GroupRetrieveUpdateDelete.as_view(), name="group-delete"),
]