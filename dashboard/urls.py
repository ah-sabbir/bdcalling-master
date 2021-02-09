
from django.urls import path, include
from dashboard import views
urlpatterns = [
    path('',views.home.as_view()),
    path('pivot-table',views.ptable, name = "pivot_table"),
]
