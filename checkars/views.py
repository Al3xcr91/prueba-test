from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from checkars import models
from checkars import serializers


class CheckarsSiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Checkars Cars site to be viewed.
    """
    queryset = models.CheckarsSite.objects.all()
    serializer_class = serializers.CheckarsSiteSerializer

    def retrieve(self, request, pk=None):
        if pk >= '17491' and pk <= '17493':
            queryset = models.CheckarsSite.objects.all()
            car = get_object_or_404(queryset, pk=pk)
            serializer = serializers.CheckarsSiteSerializer(car)
            return Response(serializer.data)
        else:
            return Response('El car_id no existe')


class CheckarsSiteViewSetById(viewsets.ModelViewSet):
    """
    API endpoint that allows Checkars Cars site to be viewed or edited.
    """
    queryset = models.CheckarsSiteByID.objects.all()
    serializer_class = serializers.CheckarsSiteSerializerById

    def update(self, request, pk=None):
        if pk == '5e14f581bf0d686228f6436a' or pk == '5e14f581bf0d686228f6436c':
            serializer = serializers.CheckarsSiteSerializerById(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = self.get_object()
            instance.precio = request.data.get("precio")
            instance.kilometros = request.data.get("kilometros")
            instance.save()
            return Response(serializer.data)
        elif pk == '5e14f581bf0d686228f6436b':
            return Response('Error: El auto no se puede actualizar')
        else:
            return Response('El _id no existe')


    def retrieve(self, request, pk=None):
        return Response('Método no permitido')

    def post(self, request, pk=None):
        return Response('Método no permitido')


class MeliItemView(viewsets.ModelViewSet):
    """
    API endpoint that allows Meli Item site to be viewed or edited.
    """
    queryset = models.MeliItem.objects.all()
    serializer_class = serializers.MeliItemSerializer

    def update(self, request, pk=None):
        if pk == 'MLA851699685':
            serializer = serializers.MeliItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if request.data.get('seller_id') == '111111':
                instance = self.get_object()
                instance.precio = request.data.get("precio")
                instance.kilometros = request.data.get("kilometros")
                instance.save()
                return Response(serializer.data)
            else:
                return Response('El seller_id no existe o es incorrecto')
        elif pk == 'MLA851699686':
            serializer = serializers.MeliItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if request.data.get('seller_id') != '222222':
                return Response('El seller_id no existe o es incorrecto')
            return Response('La publicación está pausada, no se puede actualizar')
        else:
            return Response('El mlid no existe')

    def retrieve(self, request, pk=None):
        return Response('Método no permitido')


    def get(self, request, pk=None):
        return Response('Método no permitido')
class MeliApi(viewsets.ModelViewSet):
    queryset = models.MeliApi.objects.all()
    serializer_class = serializers.MeliApiSerializer

    def retrieve(self, request, pk=None):
        if pk == 'MLA851699686' or pk == 'MLA851699685':
            queryset = models.MeliApi.objects.all()
            car = get_object_or_404(queryset, pk=pk)
            serializer = serializers.MeliApiSerializer(car)
            return Response(serializer.data)
        else:
            return Response('El car_id no existe')

    def update(self, request, pk=None):
        return Response('Método no permitido')

    def get(self, request, pk=None):
        return Response('Método no permitido')