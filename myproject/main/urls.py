from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('time/', views.time_page, name='time_page'),
    path('calc/', views.calc_page, name='calc_page'),
    path('expression/', views.expression_view, name='expression'),
    path('history/', views.history_view, name='history'),
    path('delete/', views.delete_last_expression, name='delete_last_expression'),
    path('clear/', views.clear_expressions, name='clear_expressions'),
    path('new/', views.add_new_expression, name='add_new_expression'),

]