from django.urls import path, include
from . views import viewTask, createTask,updateTask, deleteTask, registerUser, loginUser,logoutUser

urlpatterns = [
    path('', loginUser, name='login-user'),
    path('tasks/', viewTask, name='all-task'),
    path('create/', createTask, name='create-task'),
    path('logout/', logoutUser, name='logout-user'),
    path('register/', registerUser, name='register-user'),
    path('update/<str:pk>/', updateTask, name='update-task'),
    path('delete/<str:pk>/', deleteTask, name='delete-task'),
]
