import django
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),

    # Use default django auth views
    # Create a new directory inside the templates directory of your account application
    # and name it registration. This is the default path where the Django authentication views
    # expect your authentication templates to be.
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # # Change password urls
    # path('password_change/', auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),

    # # reset password urls
    # path('password_reset/', auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('reset/done', auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),

    # you can use this line instead all default django auth views in above
    path('', include('django.contrib.auth.urls')),

    # Add dashboard url to handle login and logout
    path('', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),

    path('edit/', views.edit, name='edit'),
]
