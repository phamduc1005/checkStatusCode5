from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from checkStatus.models.test import Test
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
    if data["onlyMain"]:
        pages = pages.exclude(isMain=False)
        
        pingTest.onlyMain = True
        pingTest.save()

    checkStatusAllPages(pages, pingTest)
    
    return HttpResponse('ok')






