from django.contrib import admin
from .models.test import Test
from .models.page import Page
from .models.page_type import PageType
from .models.ping_test import PingTest
from .models.ping_test_page import PingTestPage
# Register your models here.
admin.site.register(Test)
admin.site.register(PageType)
admin.site.register(Page)
admin.site.register(PingTest)
admin.site.register(PingTestPage)