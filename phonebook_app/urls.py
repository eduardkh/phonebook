from django.urls import path
from . import views


urlpatterns = [
    path('', views.phone_list, name='phone_list'),
    path('detail/', views.phone_detail, name='phone_detail'),
    path('create/', views.phone_create, name='phone_create'),
    path('update/', views.phone_update, name='phone_update'),
    path('delete/', views.phone_delete, name='phone_delete'),
]
