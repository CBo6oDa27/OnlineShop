from django.urls import path
from django.contrib.auth.views import LogoutView
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, CustomLoginView, PasswordRecoveryView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery')
]