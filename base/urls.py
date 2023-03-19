from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.home, name='home'),
    path('post/<str:pk>', views.post, name='post'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<str:pk>', views.updatePost, name='update-post'),
    path('delete-post/<str:pk>', views.delete, name='delete-post'),
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
