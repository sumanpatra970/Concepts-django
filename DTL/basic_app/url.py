from django.urls import path

from basic_app import views

urlpatterns=[
    path('appp',views.home),
]