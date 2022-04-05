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



@api_view(['POST'])
def nameTest(request):

    # # data=request.data

    # # newTest = Test.objects.create(name= data['name'])
    # # newPageType = newTest.testType.create(type = data['type'])
    
    # # newPingTest = newTest.testPing.create()
    # # count = len(data['testLink'])

    # # for element in data['testLink']:
    # #     if element['isMain'] == True:
    # #         newPage = newPageType.testLink.create(link = element['link'], isMain = element['isMain'])

    # #         response =requests.get(element['link'])
    # #         statusCode = response.status_code
    # #         roundTrip = response.elapsed.total_seconds()

    # #         PingTestPage.objects.create(pingTest = newPingTest, page = newPage, status = statusCode, loadingTime = roundTrip)
            
    # #         if roundTrip <= 3 and statusCode in range(200, 300):
    # #             newTest.testPing.update(percentSuccess = 100)




    # data = request.data
    # idTest = Test.objects.get(name = data['name'])

    # idPingTest = PingTest.objects.create(test = idTest)

    # listTypePage = PageType.objects.filter(test = idTest)



    # countSuccess = 0
    # count = 0

    # listTypePageTrue = []


    # for element in listTypePage:
    #     listPageTrue = Page.objects.filter(pageType = element, isMain = True)
        
    #     for pageTrue in listPageTrue:
    #         listTypePageTrue.append(element.id)

    #         response = requests.get(pageTrue.link)
    #         statusCode = response.status_code
    #         roundTrip = response.elapsed.total_seconds()
            
    #         if roundTrip <= 3 and statusCode in range(200, 300):
    #             countSuccess += 1
            
    #         PingTestPage.objects.create(pingTest = idPingTest, page = pageTrue, status = statusCode, loadingTime = roundTrip)
    #         count += 1
            
        

    # listTypePageFalse = PageType.objects.filter(test=idTest).exclude(id__in=listTypePageTrue)
    # for elementFalse in listTypePageFalse:
    #     listPageFalse = Page.objects.filter(pageType = elementFalse, isMain = False)

    #     for pageFalse in listPageFalse:
    #         response = requests.get(pageFalse.link)
    #         statusCode = response.status_code
    #         roundTrip = response.elapsed.total_seconds()
            
    #         if roundTrip <= 3 and statusCode in range(200, 300):
    #             countSuccess += 1

    #         PingTestPage.objects.create(pingTest = idPingTest, page = pageFalse, status = statusCode, loadingTime = roundTrip)
    #         count += 1


    # result = round((countSuccess/ count)*100)
    # PingTest.objects.filter(id = idPingTest.id).update(percentSuccess = result)

    data = request.data
    idTest = Test.objects.get(name = data['name'])

    idPingTest = PingTest.objects.create(test = idTest)


    countSuccess = 0
    count = 0

    pages = Page.objects.filter(pageType__test=idTest)
    if data['onlyMain'] == True:
        pages = pages.exclude(isMain=False)

        for page in pages:
            response = requests.get(page.link)
            statusCode = response.status_code
            roundTrip = response.elapsed.total_seconds()
            
            if roundTrip <= 3 and statusCode in range(200, 300):
                countSuccess += 1

            PingTestPage.objects.create(pingTest = idPingTest, page = page, status = statusCode, loadingTime = roundTrip)
            count += 1


    else:
        for page in pages:
            response = requests.get(page.link)
            statusCode = response.status_code
            roundTrip = response.elapsed.total_seconds()
            
            if roundTrip <= 3 and statusCode in range(200, 300):
                countSuccess += 1

            PingTestPage.objects.create(pingTest = idPingTest, page = page, status = statusCode, loadingTime = roundTrip)
            count += 1

    result = round((countSuccess/ count)*100)
    PingTest.objects.filter(id = idPingTest.id).update(percentSuccess = result)
    
    return HttpResponse('ok')

    
