
from django.urls import path

from news import views

urlpatterns = [
    path('',views.index),
    path('allnews',views.allnews),
    path('allcategory',views.allcategory)
]
