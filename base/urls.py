from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>', views.post, name='post'),
] +  static(settings.MEDIA_URL,
             document_root=settings.MEDIA_ROOT)
