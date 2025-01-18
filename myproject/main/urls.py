from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('time/', views.time_page, name='time_page'),
    path('calc/', views.calc_page, name='calc_page'),
    path('expression/', views.expression_view, name='expression'),
    path('history/', views.history_view, name='history'),
    path('delete/', views.delete_last_expression, name='delete_last_expression'),
    path('clear/', views.clear_expressions, name='clear_expressions'),
    path('new/', views.add_new_expression, name='add_new_expression'),
    path('str2words/', views.str2words, name='str2words'),
    path('str_history/', views.str_history, name='str_history'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('clicker/', views.clicker_view, name='clicker'),
    path('update/<str:parameter>/', views.update_parameter, name='update_parameter'),
]