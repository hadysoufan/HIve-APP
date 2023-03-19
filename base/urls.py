from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('post/<str:pk>', views.post, name='post'),

    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<str:pk>', views.updatePost, name='update-post'),
    path('delete/<str:pk>', views.delete, name='delete'),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
