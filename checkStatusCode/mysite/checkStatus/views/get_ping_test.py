from rest_framework.decorators import api_view
from rest_framework.response import Response

from checkStatus.models.test import Test
from checkStatus.serializers.ping_test_serializer import PingTestSerializer
from checkStatus.models.ping_test import PingTest


@api_view(['GET'])
def checkLastUrlAll(request):
    pingTestsLast = []
    tests = Test.objects.all()
    
    for test in tests:
        pingTest = PingTest.objects.filter(test = test).last()
        pingTestsLast.append(pingTest)
    
    serializer = PingTestSerializer(pingTestsLast, many=True)
    return Response(serializer.data)
