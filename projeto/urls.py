"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

    This file contains the urls for our website.
"""
from django.contrib import admin
from django.urls import include, path

# Every path call takes 2 args: string for url and a function for a view
# The view must take an HTTPRequest as an arg and return an HTTPResponse
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('recipes/', include('recipes.urls'))
]
