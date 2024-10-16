from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('accounts/', include('accounts.urls')),
    path('chat/', include('chat.urls')),
]
