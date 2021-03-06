from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('teams/', views.TeamList.as_view(), name="team_list"),
    path('teams/new/', views.TeamCreate.as_view(), name="team_create"),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name="team_detail"),
    path('teams/<int:pk>/update',
         views.TeamUpdate.as_view(), name="team_update"),
    path('teams/<int:pk>/delete',
         views.TeamDelete.as_view(), name="team_delete"),
    path('teams/<int:pk>/players/new/',
         views.PlayerCreate.as_view(), name="player_create"),
    path('favplayers/<int:pk>/players/<int:player_pk>/',
         views.FavPlayerPlayerAssoc.as_view(), name="favplayer_player_assoc"),
    path('favplayers/new/', views.FavPlayerCreate.as_view(), name="favplayer_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]