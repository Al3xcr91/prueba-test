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
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = models.CheckarsSiteByID
        fields = '__all__'


class MeliItemSerializer(serializers.ModelSerializer):
    """
        Test simulator Meli Site
    """
    seller_id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True)
    mlid = serializers.CharField(read_only=True)
    class Meta:
        model = models.MeliItem
        fields = '__all__'

class MeliApiSerializer(serializers.ModelSerializer):
    """
        Test simulator Meli Api
    """
    seller_id = serializers.IntegerField()
    status = serializers.CharField(max_length=20)
    mlid = serializers.CharField(max_length=50)
    class Meta:
        model = models.MeliApi
        fields = '__all__'