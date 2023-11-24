from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_list/', views.add_list, name='add_list'),
    path('create_user_view', views.create_user_view, name='create_user_view'),
    path('<int:list_id>/edit_list_view/', views.edit_list_view, name='edit_list_view'),
    path('<int:list_id>/done_view/', views.done_view, name='done_view'),
]