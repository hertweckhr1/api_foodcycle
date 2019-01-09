from django.urls import path, include
from rest_framework.routers import DefaultRouter

from donation import views

router = DefaultRouter()

app_name = 'donation'

urlpatterns = [
    path('', include(router.urls))
]
