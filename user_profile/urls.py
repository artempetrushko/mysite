from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetail.as_view()),
    path('cycles/', views.CycleList.as_view()),
    path('cycles/<pk>', views.CycleDetail.as_view()),
    path('boosts/', views.BoostList.as_view()),
    path('boosts/<pk>', views.BoostDetail.as_view()),
    path('click/', views.callClick, name="click"),
    path('buyBoost/', views.buyBoost, name="buyBoost"),
    path('payForBoost', views.payForBoost, name="payForBoost"),
]
