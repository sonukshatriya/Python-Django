from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='register'),
    path('insertdata', views.insertdata, name='insertdata'),
    path('output', views.output, name='output'),
    path('manageproducts', views.manageproducts, name='manageproducts'),
]
