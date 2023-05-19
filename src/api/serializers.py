from rest_framework import serializers
from . import models


class SeruSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seru
        fields = '__all__'