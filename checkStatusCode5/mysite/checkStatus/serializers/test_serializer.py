from rest_framework import serializers
from checkStatus.models.test import Test
from .page_type_serializer import PageTypeSerializer
from .ping_test_serializer import PingTestSerializer

class TestSerializer(serializers.ModelSerializer):
    testTye = PageTypeSerializer(many=True)
    testPing = PingTestSerializer(many=True)
    class Meta:
        model = Test
        fields = '__all__' 

    