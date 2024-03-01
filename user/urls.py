from django.urls import path
from .views import user_login, home, user_logout, UserListAPIView, serzhan
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', user_login, name='login'),
    path('home/', home, name='home'),
    path('tserzhan/', serzhan, name='serzhan'),
    path('logout/', user_logout, name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('api/users/', UserListAPIView.as_view(), name='user-list'),
]
