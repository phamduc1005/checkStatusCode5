from rest_framework import serializers
from checkStatus.models.page import Page
from .ping_test_page_serializer import PingTestPageSerializer

class PageSerializer(serializers.ModelSerializer):
    linkOfPage = PingTestPageSerializer(many=True, read_only=True)
    class Meta:
        model = Page
        fields = ('link', 'linkOfPage')