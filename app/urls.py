from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/submit/', views.signup, name='signup'),
    path('login/submit/', views.login, name='login'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('borrow/<str:title>/', views.borrowed, name='borrowed'),
    path('return/<str:title>/', views.return_book, name='return_book'),
]
