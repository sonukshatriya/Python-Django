from django.urls import path
from newsapp import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index),
    path('sports.html', views.sports),
    path('search', views.search),
    path('technology.html', views.technology),
    path('politics.html', views.politics)

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

