from rest_framework import serializers
from web_app.models import ScrapData


class ScrapDataserializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapData
        fields = ['nome_autor','citacao']