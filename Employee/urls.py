
from django.urls import path, include
from Employee import views

urlpatterns = [
    path('',views.home.as_view()),
]
