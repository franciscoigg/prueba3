
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TatuadorViewSet, ClienteViewSet, CitaViewSet

router = DefaultRouter()
router.register(r'tatuadores', TatuadorViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'citas', CitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]