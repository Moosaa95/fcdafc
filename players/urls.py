from django.urls import path 
from . import views 
from .endpoints import (
    GetPlayerAPIView,

)


urlpatterns = [
    path("", views.HomeView.as_view(), name='home-page'),
    path("get_player", GetPlayerAPIView.as_view(), name="get_player"),
    path("player/<int:pk>", views.PlayerDetail.as_view(), name="get_player_detail")
]
