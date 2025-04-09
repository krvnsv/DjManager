from django.urls import path

from . import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.project, name='project'),
    path('<uuid:pk>/edit/', views.edit, name='edit'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
    path('<uuid:project_id>/upload_file/', views.upload_file, name='upload_file'),
    path('<uuid:project_id>/<uuid:pk>/delete/', views.delete_file, name='delete_file'),
    path('<uuid:project_id>/add_note/', views.add_note, name='add_note'),
]