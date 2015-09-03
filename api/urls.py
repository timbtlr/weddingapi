from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^s3direct/', include('s3direct.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('photo.urls')),
    url(r'^', include('rsvp.urls')),
    url(r'^', include('registry.urls')),
)
