from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.urls import path, re_path
from django.urls import path, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('docs/', views.docs_view, name='docs'),
    re_path(r'^docs/(?P<path>.*)/$', views.docs_redirect, name='docs_redirect'),
]