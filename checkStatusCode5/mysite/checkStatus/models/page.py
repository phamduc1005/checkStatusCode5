from enum import Flag
from django.db import models
from .page_type import PageType

class Page(models.Model):
    pageType = models.ForeignKey(PageType, related_name='testLink', on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    isMain = models.BooleanField(default=False)

    # class Meta:
    #     db_table = 'page'

    def __str__(self):
        return self.pageType.type + ' ' + self.link
        