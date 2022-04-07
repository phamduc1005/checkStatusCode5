from rest_framework import serializers
from checkStatus.models.page_type import PageType
from .page_serializer import PageSerializer

class PageTypeSerializer(serializers.ModelSerializer):
    testLink = PageSerializer(many=True, read_only=True)
    class Meta:
        model = PageType
        fields = ('type', 'testLink')