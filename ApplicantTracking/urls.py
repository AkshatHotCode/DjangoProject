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
    path('account', views.account, name="account"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('addopenings', views.addopenings, name="addopenings"),
    path('addcandidates', views.addcandidates, name="addcandidates"),
    path('addpipeline', views.addpipeline, name="addpipeline"),
    path('addplacement', views.addplacement, name="addplacement"),
    path('addaccount', views.addaccount, name="addaccount"),
]
