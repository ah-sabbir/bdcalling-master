
from django.urls import path, include
from income_deliveris import views

urlpatterns = [
    path('',views.home.as_view()),
    path('incoming-report',views.income.as_view(),name="incoming_report"),

]
