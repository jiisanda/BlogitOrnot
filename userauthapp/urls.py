from django.urls import path
from userauthapp import views
from .views import ProfileEditView, PasswordsChangeView, PasswordSuccessView, ShowProfilePageView

# app_name="UserAuthApp"
# TEMPLATE URLS
urlpatterns = [
    path('user_login/', views.user_login, name="user_login"),
    path('register/', views.registrationView, name='register'),
    path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', views.PasswordSuccessView, name='password_changed'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
]
