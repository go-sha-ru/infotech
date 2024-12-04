from rest_framework import serializers

from core.models import Data


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['ne', 'address', 'coordinates', 'technology', 'status']