from django.urls import path
from . import views
urlpatterns = [
    path('', views.WelcomeAuthView.as_view(), name='welcome_auth'),
]