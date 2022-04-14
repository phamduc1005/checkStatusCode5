from rest_framework.decorators import api_view
from rest_framework.response import Response

from checkStatus.models.test import Test
from checkStatus.models.ping_test import PingTest
from checkStatus.models.ping_test_page import PingTestPage
from checkStatus.serializers.ping_test_page_serializer import PingTestPageSerializer


@api_view(['GET'])
def checkAllUrlOfAWeb(request, testName):
    test = Test.objects.get(name=testName)
    
    pingTest = PingTest.objects.filter(test=test).last()
    
    pingTestsPage = PingTestPage.objects.filter(pingTest=pingTest).order_by('-status')
    serializer = PingTestPageSerializer(pingTestsPage, many=True)
    
    return Response(serializer.data)
