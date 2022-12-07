from django.urls import path
from . import views

urlpatterns = [
  #path('login', views.index, name="login"),
  path('user_overview', views.user_overview, name="user_overview"),
  path('user_create', views.user_create, name="user_create"),
  path('user_edit/<str:pk>', views.user_edit, name="user_edit"),
  #url sotto creato per test di doppia pagina create - edit
  path('user_update/<str:pk>', views.user_update, name="user_update"),
  #path('user_add', views.user_add, name='user_add'),
  path('index', views.index, name="index"),
  path('info', views.info, name="info"),
  path('profile/<str:pk>', views.profile, name="profile"),
  path('adweb', views.adweb, name="adweb"),
  path('iteratti', views.iteratti, name="iteratti"),
  path('sdi', views.sdi, name="sdi"),
  
 ] 