from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post-job/', views.post_job, name='post_job'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('applications/<int:job_id>/', views.applications, name='applications'),
    path('update/<int:app_id>/<str:status>/', views.update_status),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
]
