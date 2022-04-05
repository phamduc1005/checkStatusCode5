from rest_framework import serializers
from checkStatus.models.ping_test_page import PingTestPage

class PingTestPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PingTestPage
        fields = '__all__'
        read_only_fields = ('status', 'loadingTime')