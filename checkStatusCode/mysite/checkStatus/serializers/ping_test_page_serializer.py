from rest_framework import serializers
from checkStatus.models.ping_test_page import PingTestPage

class PingTestPageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source = 'page.link')
    class Meta:
        model = PingTestPage
        fields = ('url', 'status', 'loadingTime')
        read_only_fields = ('status', 'loadingTime')