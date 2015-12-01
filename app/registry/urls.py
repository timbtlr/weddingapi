from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
]

router = DefaultRouter()
router.register(prefix='registry-items', viewset=views.RegistryItemViewSet, base_name='registry-items')

urlpatterns += router.urls