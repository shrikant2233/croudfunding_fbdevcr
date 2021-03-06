"""croundfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from campaigns.views import login_view, register, profile, logout_view, new_campaign, list_campaigns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_view),
    path('register', register),
    path('profile', profile),
    path('logout', logout_view),
    path('campaigns/new', new_campaign),
    path('campaigns', list_campaigns),
]
