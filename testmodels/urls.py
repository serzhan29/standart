from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestModelList

router = DefaultRouter()
router.register(r'test', TestModelList)

urlpatterns = [
    path('test-models/', include(router.urls)),
]
