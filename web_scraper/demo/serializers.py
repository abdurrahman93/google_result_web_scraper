from rest_framework import serializers
from .models import GoogleResult


class GoogleResultModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleResult
        fields = ('query_param', 'text', 'url')


class GoogleResultReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleResult
        fields = ('query_param',)
