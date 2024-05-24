from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import CustomPasswordResetView
from . import views

app_name='accounts'

urlpatterns=[
    path('login', views.login_view, name='login'),
    # login
    path('logout', views.logout_view, name='logout'),
    # logout    
    path('signup', views.signup_view, name='signup'),
    # registration / signup
    
    #Password Reset
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

