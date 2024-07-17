from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('rules/', views.rules_section, name="rules_section"),
    path('rules/basics', views.basic_mechanics, name="basic_mechanics"),
    path('bounties/', views.bounty_list, name="bounties")
]
