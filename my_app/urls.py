from django.urls import path
from my_app.views import index_view

urlpatterns = [
    path("index/", index_view),
]