from checkars import models
from rest_framework import serializers


class CheckarsSiteSerializer(serializers.ModelSerializer):
    """
        Test simulator Checkars Site
    """
    class Meta:
        model = models.CheckarsSite
        fields = '__all__'


class CheckarsSiteSerializerById(serializers.ModelSerializer):
    """
        Test simulator Checkars Site with _id
    """
    class Meta:
        model = models.CheckarsSiteByID
        fields = '__all__'


class MeliItemSerializer(serializers.ModelSerializer):
    """
        Test simulator Meli Site
    """
    class Meta:
        model = models.MeliItem
        fields = '__all__'