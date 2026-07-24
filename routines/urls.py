from django.urls import path
from . import views

app_name = 'routines'

urlpatterns = [
    path('', views.today_view, name='today'),
    path('toggle/<int:habit_id>/', views.toggle_habit, name='toggle'),
    path('stats/', views.stats_view, name='stats'),
    path('manage/', views.manage_habits, name='manage'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete'),
]
