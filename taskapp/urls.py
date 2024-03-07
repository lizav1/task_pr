from django.urls import path
from .views import home_view,create_task_view, edit_task_view, delete_task,view_task, login_view, logout, signup_view

urlpatterns = [
    path('', home_view, name='home'),

    #task urls
    path('create_task', create_task_view, name='create_task'),
    path('edit_task/<int:id>/', edit_task_view, name='edit_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('task/<int:id>/', view_task, name='task'),

    #login urls
    path('login', login_view, name='login'),
    path('logout', logout, name='logout'),
    path('signup', signup_view, name='signup'),


]
