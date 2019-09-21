"""drill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework import routers, serializers, viewsets
from steel.views import (
    fetch_all, get_units_adv, avg_turn_over, avg_chg_high_low,
    avg_open_close_by_month, turnover_by_day, neg_volatility)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fetch-all/', fetch_all, name='fetch_all'),
    path('get_units_adv/', get_units_adv, name='get_units_adv'),
    path('avg_turn_over/', avg_turn_over, name='avg_turn_over'),
    path('avg_chg_high_low/', avg_chg_high_low, name='avg_chg_high_low'),
    path('avg_open_close_by_month/', avg_open_close_by_month, name='avg_open_close_by_month'),
    path('turnover_by_day/', turnover_by_day, name='turnover_by_day'),
    path('neg_volatility/', neg_volatility, name='neg_volatility'),
]
