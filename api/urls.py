from django.urls import path

from home.views import getData

urlpatterns = [
    path('getData/',getData)
]