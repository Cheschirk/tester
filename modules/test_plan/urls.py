"""tester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views
from modules.test_plan.views import PlanListView, PlanDetailView, DashboardView, PlanNewView, PlanUpdateView

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('test_plan_new/',  PlanNewView.as_view(), name='test_plan_new'),
    path('test_plan_list/', PlanListView.as_view(), name='test_plan_list'),
    re_path(r'^test_plan_view/(?P<pk>\d+)$', PlanDetailView.as_view(), name='test_plan_view'),
    re_path(r'^test_plan_edit/(?P<pk>\d+)$', PlanUpdateView.as_view(), name='test_plan_edit'),
    ]

