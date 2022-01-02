from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListDictionary.as_view()),
    path('<int:pk>/', views.DetailDictionary.as_view()),
]