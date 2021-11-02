from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'LogService'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='App_Login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name=''), name='logout'),
    path('signup/', views.signup, name='signup'),
]
