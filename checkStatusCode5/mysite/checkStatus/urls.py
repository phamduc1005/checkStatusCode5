from checkStatus.views import test, page
from django.urls import path

urlpatterns = [
    path('check', test.nameTest, name='abc'),
    # path('abc', page.linkPage, name='abcd'),
]