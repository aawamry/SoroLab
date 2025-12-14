from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DatasetViewSet, VariableViewSet

router = DefaultRouter()
router.register(r'datasets', DatasetViewSet)
router.register(r'variables', VariableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

