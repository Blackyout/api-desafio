from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.db import connection
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Health Checks
def healthz(request):
    """App is alive"""
    return JsonResponse({"status": "ok", "service": "django-api"})

def readyz(request):
    """Database is connected"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "ready", "database": "connected"})
    except Exception:
        return JsonResponse({"status": "not_ready", "database": "error"}, status=503)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    
    # Health Checks
    path("healthz", healthz),
    path("readyz", readyz),

    # Documentación
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]