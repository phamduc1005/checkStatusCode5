from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from checkStatus.models.test import Test
from checkStatus.serializers.test_serializer import TestSerializer
from checkStatus.serializers.ping_test_serializer import PingTestSerializer
from checkStatus.serializers.page_serializer import PageSerializer
from rest_framework import status

from checkStatus.models.page_type import PageType
from checkStatus.models.ping_test import PingTest
from checkStatus.models.ping_test_page import PingTestPage
from checkStatus.models.page import Page

def checkStatus(page):
    response = requests.get(page.link)
    statusCode = response.status_code
    loadingTime = response.elapsed.total_seconds()
    
    return statusCode, loadingTime

def checkStatusAllPages(pages, pingTest):
    nbSuccess = 0

    for page in pages:
        statusCode, loadingTime = checkStatus(page)
        PingTestPage.objects.create(pingTest = pingTest, page = page, status = statusCode, loadingTime = loadingTime)
        if loadingTime <= 3 and statusCode in range(200, 300):
            nbSuccess += 1

    rate = round((nbSuccess/ len(pages))*100)
    pingTest.percentSuccess = rate
    pingTest.save()



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




@api_view(['GET'])
def checkLastUrlAll(request):
    listData = []
    test = Test.objects.all()
    for element in test:
        pingTest = PingTest.objects.filter(test = element).last()
        data = {
            'test' : element.name,
            'percentSuccess' : pingTest.percentSuccess, 
            'createdAt' : pingTest.createdAt
        }

        listData.append(data)

    return Response(listData)




@api_view(['GET'])
def checksAllUrlOfAWeb(request, nameTest):
    listData = []
    
    test = Test.objects.get(name=nameTest)
    pageTypes = PageType.objects.filter(test=test)
    pingTest = PingTest.objects.filter(test=test).last()
    
    for element in pageTypes:
        pages = Page.objects.filter(pageType=element)
        for page in pages:
            pingTestPage = PingTestPage.objects.get(page=page, pingTest=pingTest)

            data = {
                'url' : page.link,
                'status' : pingTestPage.status,
                'loadingTime' : pingTestPage.loadingTime
            }

            listData.append(data)

    return Response(listData)
    
