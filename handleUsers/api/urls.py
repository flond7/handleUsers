from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name="api-overwiev"),
  #path('login', views.index, name="login"),
  path('user_overview', views.user_overview, name="user_overview"),
  path('user_create', views.user_create, name="user_create"),
  path('user_add', views.user_add, name='user_add'),
  path('index', views.index, name="index"),
  #path('profile', views.profile, name="profile"),
  path('profile/<str:pk>', views.profile, name="profile"),
  path('adweb', views.adweb, name="adweb"),
  
 ] 