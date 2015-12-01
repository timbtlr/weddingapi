from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
]

router = DefaultRouter()
router.register(prefix='rsvps', viewset=views.RsvpViewSet, base_name='rsvps')

urlpatterns += router.urls