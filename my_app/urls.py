from django.urls import path
from my_app.views import index_view, my_app_detail_views
urlpatterns = [
    path("index/", index_view),
    path("detail/<int:my_app_id>", my_app_detail_views)
]