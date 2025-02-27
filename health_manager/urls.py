from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import openapi
from drf_yasg import openapi as yasg_openapi
from drf_yasg.views import get_schema_view
from .views import MedicationViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'medications', MedicationViewSet, basename='medication')
router.register(r'reminders', ReminderViewSet, basename='reminder')

schema_view = get_schema_view(
    openapi.Info(
        title="Health Manager API",
        default_version='v1',
        description="API documentation for Health Manager",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@healthmanager.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
