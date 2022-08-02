from django.urls import path
from . import views
urlpatterns = [
    path('', views.WelcomeOrderView.as_view(), name='welcome_order'),
]