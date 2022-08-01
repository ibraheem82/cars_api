from django.urls import path
from . import views
urlpatterns = [
    path('auth/', views.WelcomeAuthView.as_view(), name='welcome_auth'),
]