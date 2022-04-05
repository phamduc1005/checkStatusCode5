from rest_framework import serializers
from checkStatus.models.ping_test import PingTest
from .ping_test_page_serializer import PingTestPageSerializer

class PingTestSerializer(serializers.ModelSerializer):
    pingTestStatus = PingTestPageSerializer(many=True)
    class Meta:
        model = PingTest
        fields = '__all__'
        read_only_fields = ('createdAt', 'percentSuccess')



