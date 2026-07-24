from django.urls import path
from . import views

app_name = 'routines'

urlpatterns = [
    path('', views.today_view, name='today'),
    path('toggle/<int:habit_id>/', views.toggle_habit, name='toggle'),
    path('stats/', views.stats_view, name='stats'),
]
