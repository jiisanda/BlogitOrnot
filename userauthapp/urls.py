from os import name
from django.urls import path
from userauthapp import views
from .views import ProfileEditView, PasswordsChangeView, PasswordSuccessView

# app_name="UserAuthApp"
# TEMPLATE URLS
urlpatterns = [
    path('user_login/', views.user_login, name="user_login"),
    path('register/', views.registrationView, name='register'),
    path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='userauthapp/change_password.html'), name='change_password'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', views.PasswordSuccessView, name='password_changed'),
]
