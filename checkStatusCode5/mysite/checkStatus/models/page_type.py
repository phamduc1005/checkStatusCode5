from pyexpat import model
from django.db import models
from .test import Test

class PageType(models.Model):
    test = models.ForeignKey(Test, related_name='testType', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)

    # class Meta:
    #     db_table = 'pageType'

    def __str__(self):
        return self.test.name + ' ' + self.type
        