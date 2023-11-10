from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name = "home"),
    path('signup/',views.signup, name = "signup"),
    path('login/',auth_views.LoginView.as_view(template_name = "goodaau/login.html" ,authentication_form = (LoginForm)), name = "login"),
    path('logout/',auth_views.LogoutView.as_view(), name = "logout"),
    path('online-application-form/',views.application, name = "application"),
    path('user-profile/',views.userProfile, name='profile'),
    path('edit-profile/', views.userDetailEdit, name="edit-profile"),
     path('payment/', views.paypal_payment, name = "payment"),
    path('payment_done/', views.payment_done, name = "payment_done"),
    path('payment_cancelled/', views.payment_cancelled, name = "payment_cancelled"),
]
