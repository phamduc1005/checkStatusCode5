from checkStatus.views import views
from django.urls import path

urlpatterns = [
    path('check', views.checkStatusCode, name='checkStatusCode'),
    path('checkLastUrlAll/', views.checkLastUrlAll, name='checkLastUrlAll'),
    path('allChecksOfAWebsite/<str:nameTest>/', views.checksAllUrlOfAWeb, name='allChecksOfACebsite'),
]