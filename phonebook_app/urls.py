from django.urls import path, re_path
from . import views

app_name = 'phone'

urlpatterns = [
    path('', views.phone_list, name='phone_list'),
    re_path('detail/(?P<pk>\d+)/', views.phone_detail, name='phone_detail'),
    path('create/', views.phone_create, name='phone_create'),
    re_path('edit/(?P<pk>\d+)/', views.phone_update, name='phone_update'),
    re_path('delete/(?P<pk>\d+)/', views.phone_delete, name='phone_delete'),
]
