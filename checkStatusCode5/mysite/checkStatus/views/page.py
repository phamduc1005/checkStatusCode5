# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import requests
# from checkStatus.models.page import Page
# from checkStatus.serializers.page_serializer import PageSerializer
# from rest_framework import status
# from checkStatus.models.ping_test_page import PingTestPage
# from checkStatus.models.test import Test
# from checkStatus.serializers.test_serializer import TestSerializer

# @api_view(['GET'])
# def linkPage(request):
#     # data=request.data
#     # idLink = data['id']

#     # PingTestPage.objects.create()

#     # serializer = PageSerializer(data)
#     # if serializer.is_valid():
#     c = TestSerializer(many=True)
#     return Response(list(c), safe=False)