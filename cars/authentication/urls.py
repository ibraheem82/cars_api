from django.urls import path
from . import views
urlpatterns = [
    path('', views.WelcomeAuthView.as_view(), name='welcome_auth'),
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
]