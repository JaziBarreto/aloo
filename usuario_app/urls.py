from django.urls import path     
from . import views #means that views is in the same directory as this
from .views import video

app_name = 'usuario_app'

urlpatterns = [
    path('', views.video, name='index'),
    path('login', views.autenticationView, name='login'),
    path('logout', views.logOutView, name='logout'),
    path('register', views.register, name='register'),
    path('edit', views.editPerfil, name='editPerfil')
    
]
