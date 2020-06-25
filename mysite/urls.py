from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers, serializers, viewsets
from checkars import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'test/api/v1/site', views.CheckarsSiteViewSet)
router.register(r'test/api/v1/site-by-id', views.CheckarsSiteViewSetById)
router.register(r'test/api/v1/meli', views.MeliItemView)
router.register(r'test/api/v1/meli-api', views.MeliApi)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
