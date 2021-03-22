from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.BasePage.as_view(), name='base_page'),
    path('', views.IndexPageView.as_view(), name='title-list'),
    path('', views.FooterPartView.as_view()),
]
