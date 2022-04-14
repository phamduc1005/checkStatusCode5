from checkStatus.views import post_check_status
from checkStatus.views import get_ping_test_page
from checkStatus.views import get_ping_test

from django.urls import path

urlpatterns = [
    path('check', post_check_status.checkStatusCode, name='checkStatusCode'),
    path('checkLastUrlAll/', get_ping_test.checkLastUrlAll, name='checkLastUrlAll'),
    path('allCheckOfAWebsite/<str:testName>/', get_ping_test_page.checkAllUrlOfAWeb, name='allCheckOfAWebsite'),
]
