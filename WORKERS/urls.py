from django.urls import path

from WORKERS import views


urlpatterns = [

    path('WR/', views.worker_signup, name="worker_reg"),
    path('WL/', views.worker_login, name="worker_login"),
    path('WH/',views.worker_home,name="worker_home"),



]