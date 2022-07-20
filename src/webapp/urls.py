
from .views import hello, index, like
from django.urls import path

urlpatterns = [
    path('hello/', hello),
    path('', index),
    path('like/', like)
]