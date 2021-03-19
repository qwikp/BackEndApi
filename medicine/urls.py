from django.urls import include, path
from django.contrib import admin
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
]