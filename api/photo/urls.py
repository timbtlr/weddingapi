from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
]

router = DefaultRouter()
router.register(prefix='photos', viewset=views.PhotoViewSet, base_name='photos')

urlpatterns += router.urls