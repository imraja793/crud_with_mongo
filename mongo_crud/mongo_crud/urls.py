"""mongo_crud URL Configuration

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

from crud.views import CreateStudent, Search, DeleteData, DeleteAllData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CreateStudent/<int:pk>', CreateStudent.as_view(), name="create"),
    # path('Same/', Same.as_view(), name="Same"),
    path('DeleteData/<int:pk>', DeleteData.as_view(), name="DeleteData"),
    path('Search/', Search.as_view(), name="Search"),
    path('DeleteAllData/', DeleteAllData.as_view(), name="DeleteAllData"),

]
