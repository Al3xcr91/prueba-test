from rest_framework import viewsets
from checkars import models
from checkars import serializers


class CheckarsSiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Checkars Cars site to be viewed.
    """
    queryset = models.CheckarsSite.objects.all()
    serializer_class = serializers.CheckarsSiteSerializer


class CheckarsSiteViewSetById(viewsets.ModelViewSet):
    """
    API endpoint that allows Checkars Cars site to be viewed or edited.
    """
    queryset = models.CheckarsSiteByID.objects.all()
    serializer_class = serializers.CheckarsSiteSerializerById


class MeliItemView(viewsets.ModelViewSet):
    """
    API endpoint that allows Meli Item site to be viewed or edited.
    """
    queryset = models.MeliItem.objects.all()
    serializer_class = serializers.MeliItemSerializer
