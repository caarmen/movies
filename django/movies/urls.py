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
from movies.views import full, manytomany, manytoone, onetomany, onetoone

urlpatterns = [
    path("admin/", admin.site.urls),
    path("onetoone/nplus1/", onetoone.nplus1),
    path("onetoone/optim/", onetoone.optim),
    path("manytoone/nplus1/", manytoone.nplus1),
    path("manytoone/optim/", manytoone.optim),
    path("onetomany/nplus1/", onetomany.nplus1),
    path("onetomany/optim/", onetomany.optim),
    path("manytomany/nplus1/", manytomany.nplus1),
    path("manytomany/optim/", manytomany.optim),
    path("full/nplus1/", full.nplus1),
    path("full/optim/", full.optim),
] + debug_toolbar_urls()
