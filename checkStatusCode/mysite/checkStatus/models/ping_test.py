from django.db import models
from .test import Test
from datetime import datetime

class PingTest(models.Model):
    test = models.ForeignKey(Test, related_name='testPing', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now)
    percentSuccess = models.IntegerField(default=0)
    onlyMain = models.BooleanField(default=False)

    def __str__(self):
        return self.test.name + ' ' + str(self.createdAt) + ' ' + str(self.onlyMain)