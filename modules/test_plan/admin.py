from django.contrib import admin

from .models import TestPlan, PlanCase, PlanLog

admin.site.register(TestPlan)
admin.site.register(PlanCase)
admin.site.register(PlanLog)
