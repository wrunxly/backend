from django.contrib import admin
from django.urls import path, include
from apps.profile.views.auth_views import *
from django.views.static import serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Coofis API Documentation",
        default_version='v1',
        description="Documentation for Coofis API",
        contact=openapi.Contact(email="coofis@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path("admin/", admin.site.urls),
    path('api/', include([
        path('profile/', include('apps.profile.urls')),
        path('divisi/', include('apps.divisi.urls')),
        path('departemen/', include('apps.departemen.urls')),
        path('jabatan/', include('apps.jabatan.urls')),
        path(
        "auth/",
        include(
            [
                path("login/", LoginView.as_view(), name="auth-login"),
                path("register/", RegisterView.as_view(), name="auth-register"),
                path("logout/", LogoutView.as_view(), name="auth-logout"),
            ]
        ),
    ),
        path('lampiran/', include('apps.lampiran.urls')),
        path('surat/', include('apps.surat.urls')),
        path('group/', include('apps.group.urls')),
    ])),
]
