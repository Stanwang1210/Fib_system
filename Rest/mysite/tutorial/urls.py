from django.urls import path, re_path

from .views import FibCalView

urlpatterns = [
    re_path(r'^tutorial/?$', FibCalView.as_view(), name='create'),
]
