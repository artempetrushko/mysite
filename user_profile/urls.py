from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('click/', views.callClick, name="click"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout),
    path('registration/', views.user_registration, name="registration"),
    path('users/', views.UserViewSet.as_view()),
    path('user/<pk>/', views.UserView.as_view()),
]
