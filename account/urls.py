from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = "account"
urlpatterns = [
    # Login page
    # path('', auth_views.LoginView.as_view(template_name='account/nporegister.html'), name = 'login'),

    # NPO Registration and Login
    path("npo/register/", views.register_npo, name ="register-npo"),
    path("npo/login/", views.login_npo, name ="login-npo"),

    # Logout Page
    path('logout/', views.logout_view, name='logout'),

    ]