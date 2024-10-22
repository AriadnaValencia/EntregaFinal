from django.urls import path
from . import views
from .views import signup, CustomLoginView
from django.contrib.auth import views as auth_views
from .views import edit_profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('profile/', edit_profile, name='profile'),
]
