from django.urls import path
from .views import admin_dashboard, approve_worker, reject_worker,hai
from ADMIN import views


urlpatterns = [
    path('h/', views.hai,name="hii"),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve/<int:worker_id>/', views.approve_worker, name='approve_worker'),
    path('reject/<int:worker_id>/', views.reject_worker, name='reject_worker'),
]


