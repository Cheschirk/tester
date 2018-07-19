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
from modules.test_case.views import CaseListView, CaseDetailView

urlpatterns = [

    path('test_case_list/', CaseListView.as_view(), name='test_case_list'),
    path('test_case_new/', views.test_case_new, name='test_case_new'),
    path('test_case_edit/', views.test_case_edit, name='test_case_edit'),
    re_path(r'^test_case_view/(?P<pk>\d+)$', CaseDetailView.as_view(), name='test_case_view'),
    ]

