from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('navigation/', views.navigation, name='navigation'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('claw_machine/', views.claw_machine, name='claw_machine'),
    path('coollistings/', views.coollistings, name='coollistings'),
    path('wheel_of_fortune/', views.wheel_of_fortune, name='wheel_of_fortune'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
