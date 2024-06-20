from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('', views.task_list, name='task-list'),
    path('task/create/', views.task_create, name='task-create'),
    path('task/<str:pk>/view/', views.task_view, name='task-view'),
    path('task/<str:pk>/update/', views.task_update, name='task-update'),
    path('task/<str:pk>/delete/', views.task_delete, name='task-delete'),
    path('task/<str:pk>/done/', views.task_mark_as_done, name='task-done'),
    path('task/<str:pk>/undo/', views.task_undo, name='task-undo'),
]