from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("result/", views.result_view, name="result"),    
    path("", views.real_time_view, name="main"),
    path("real_time/", views.real_time_view, name="real_time")
]
