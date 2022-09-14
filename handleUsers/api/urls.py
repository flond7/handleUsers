from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name="api-overwiev"),
  #path('login', views.index, name="login"),
  path('user_overview', views.user_overview, name="user_overview"),
 ] 