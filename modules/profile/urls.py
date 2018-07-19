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
from django.urls import path, include, re_path
from . import views
from modules.profile.views import SigninView, LoginView #, UserUpdateView


urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'),
    path('login/', LoginView.as_view(), name='login'),
   # re_path(r'^user_settings/(?P<pk>\d+)$', UserUpdateView.as_view(), name='user_settings'),

    ]
