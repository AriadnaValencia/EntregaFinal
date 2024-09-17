from django.urls import path
from . import views
from .views import signup, CustomLoginView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', views.profile_view, name='profile'),
]
