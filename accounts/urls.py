from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('addUser/', views.addUser, name='addUser'),
    path('login/', views.login, name='login'),
    path('loginForm/', views.loginForm, name='loginForm'),  # Make sure this path exists
    path('logout/', views.logout, name='logout'),
]