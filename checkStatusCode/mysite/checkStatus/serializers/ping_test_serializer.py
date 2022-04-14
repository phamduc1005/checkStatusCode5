from rest_framework import serializers
from checkStatus.models.ping_test import PingTest
from .ping_test_page_serializer import PingTestPageSerializer

class PingTestSerializer(serializers.ModelSerializer):
    # pingTestStatus = PingTestPageSerializer(many=True, read_only=True)
    test = serializers.CharField(source = 'test.name')
    class Meta:
        model = PingTest
        fields = ('test', 'createdAt', 'percentSuccess', 'onlyMain')
        read_only_fields = ('createdAt', 'percentSuccess')
