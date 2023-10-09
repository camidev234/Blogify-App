from django.urls import path
from . import views as v


urlpatterns = [
    path('indexUser/', v.indexUser, name='indexUser'),
]