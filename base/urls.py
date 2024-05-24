from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login/', views.user_login, name = 'login'),
    path('signup/', views.user_signup, name = 'signup'),
    
    path('room/', views.room, name = 'room'),
    path('room_form/', views.room_form, name = 'room_form'),
    path('delete/', views.delete, name = 'delete' ),
    path('update-room/<int:pk>', views.updateRoom, name= 'update-room'),
    path('delete-room/<int:pk>', views.deleteRoom, name= 'delete-room'),
    
]
