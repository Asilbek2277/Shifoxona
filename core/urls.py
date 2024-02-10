"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from Tizim.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamma_xona/', hamma_xona),
    path('xona_ochirish/<int:pk>/', xona_ochirish),
    path('xona_tahrirlash/<int:pk>/', xona_tahrirlash),

    path('hamma_xizmatlar/', hamma_xizmatlar),
    path('xizmat_ochirish/<int:pk>/', xizmat_ochirish),
    path('xizmat_tahrirlash/<int:pk>/', xizmat_tahrirlash),

    path('hamma_shifokor/', hamma_shifokor),
    path('shifokor_ochirish/<int:pk>/', shifokor_ochirish),
    path('shifokor_tahrirlash/<int:pk>/', shifokor_tahrirlash),

    path('hamma_buyurtma/', hamma_buyurtma),
    path('buyurtma_ochirish/<int:pk>/', buyurtma_ochirish),
    path('buyurtma_tahrirlash/<int:pk>/', buyurtma_tahrirlash),

    path('hamma_bemorlar/', hamma_bemorlar),
    path('bemor_ochirish/<int:pk>/', bemor_ochirish),
    path('bemor_tahrirlash/<int:pk>/', bemor_tahrirlash),
]
