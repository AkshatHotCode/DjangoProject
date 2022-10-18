from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('openings', views.opening, name="openings"),
    path('candidates', views.candidates, name="candidates"),
    path('pipeline', views.pipeline, name="pipeline"),
    path('placement', views.placement, name="placement"),
    path('dashboard', views.dashboard, name="dashboard")
]
