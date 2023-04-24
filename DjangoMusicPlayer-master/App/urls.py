from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('upload/', views.upload, name='upload'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT}),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
]

