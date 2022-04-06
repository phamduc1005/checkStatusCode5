from checkStatus.views import test
from django.urls import path

urlpatterns = [
    path('check', test.checkStatusCode, name='checkStatusCode'),
]
