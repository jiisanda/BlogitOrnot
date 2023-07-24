from django.urls import path

from .views import (
    ProfileEditView, PasswordsChangeView, PasswordSuccessView, ShowProfilePageView, EditProfilePageView, UserLoginView, RegisterView
)


urlpatterns = [
    path('login/', UserLoginView.as_view(), name="user_login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', PasswordSuccessView, name='password_changed'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_user_profile/', EditProfilePageView.as_view(), name='edit_profile_page'),
]
