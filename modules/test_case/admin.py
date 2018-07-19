from django.contrib import admin

from .models import TestCase, CaseLog

admin.site.register(TestCase)
admin.site.register(CaseLog)
