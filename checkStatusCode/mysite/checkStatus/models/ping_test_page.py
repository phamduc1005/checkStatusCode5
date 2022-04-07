from django.db import models
from .ping_test import PingTest
from .page import Page

class PingTestPage(models.Model):
    pingTest = models.ForeignKey(PingTest, related_name='pingTestStatus', on_delete=models.CASCADE)
    page = models.ForeignKey(Page, related_name='linkOfPage', on_delete=models.CASCADE)
    status = models.IntegerField()
    loadingTime = models.IntegerField()

    def __str__(self):
        return self.page.link