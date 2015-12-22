from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []

router = DefaultRouter()
router.register(prefix='invitations', viewset=views.InvitationViewSet, base_name='invitations')
router.register(prefix='invitees', viewset=views.InviteeViewSet, base_name='invitees')

urlpatterns += router.urls