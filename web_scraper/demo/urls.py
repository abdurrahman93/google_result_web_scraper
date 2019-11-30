from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import GoogleResultApi

router = DefaultRouter()
router.register(r'', GoogleResultApi)

urlpatterns = [
    url('', include(router.urls)),
]