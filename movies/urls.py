"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path

from movies.views.full import full
from movies.views.step1 import step1
from movies.views.step2 import step2
from movies.views.step3 import step3

urlpatterns = [
    path("admin/", admin.site.urls),
    path("step1/", step1),
    path("step2/", step2),
    path("step3/", step3),
    path("full/", full),
] + debug_toolbar_urls()
