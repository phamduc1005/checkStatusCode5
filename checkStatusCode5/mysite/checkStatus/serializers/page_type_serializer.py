from rest_framework import serializers
from checkStatus.models.page_type import PageType
from .page_serializer import PageSerializer

class PageTypeSerializer(serializers.ModelSerializer):
    testLink = PageSerializer(many=True)
    class Meta:
        model = PageType
        fields = '__all__'