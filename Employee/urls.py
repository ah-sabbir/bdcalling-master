
from django.urls import path, include
from Employee import views

urlpatterns = [
    path('',views.Attendancecreate.as_view()),
]
