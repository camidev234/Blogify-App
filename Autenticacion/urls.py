from django.urls import path
from . import views as v

urlpatterns = [
    path('loginForm/', v.loginUser, name='loginUser'),
    path('signUp/', v.signUpView, name='signUpUser'),
    path('logout/', v.logout_view, name='logout'),
]