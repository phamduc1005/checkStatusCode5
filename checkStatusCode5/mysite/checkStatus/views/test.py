from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from checkStatus.models.test import Test
from checkStatus.serializers.test_serializer import TestSerializer
from rest_framework import status

from checkStatus.models.page_type import PageType
from checkStatus.models.ping_test import PingTest
from checkStatus.models.ping_test_page import PingTestPage
from checkStatus.models.page import Page



def checkStatus(page):
    response = requests.get(page.link)
    statusCode = response.status_code
    waitingTime = response.elapsed.total_seconds()
    
    return statusCode, waitingTime


def checkStatusAllPages(pages, pingTest):
    calculateSuccess = 0
    sum = 0

    for page in pages:
        statusCode, waitingTime = checkStatus(page)
        PingTestPage.objects.create(pingTest = pingTest, page = page, status = statusCode, loadingTime = waitingTime)
        if waitingTime <= 3 and statusCode in range(200, 300):
            calculateSuccess += 1
        sum += 1

    rate = round((calculateSuccess/ sum)*100)
    PingTest.objects.filter(id = pingTest.id).update(percentSuccess = rate)



@api_view(['POST'])
def checkStatusCode(request):
    data = request.data
    test = Test.objects.get(name = data['name'])

    pingTest = PingTest.objects.create(test = test)

    pages = Page.objects.filter(pageType__test=test)
    if data['onlyMain']:
        pages = pages.exclude(isMain=False)

    checkStatusAllPages(pages, pingTest)
    

    return HttpResponse('ok')


    
