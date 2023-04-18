from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.logo1,name='logo1'),
    path('about1',views.about1,name='about1'),
    path('about',views.about,name='about'),
    path('log',views.log,name='log'),
    path('add',views.add,name='add'),
    path('super',views.super,name='super'),
    path('item',views.item,name='item'),
    path('item2', views.item2, name='item2'),
    path('table', views.table, name='table'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('logout', views.logout, name='logout'),

]
