from django.urls import path
from . import views
urlpatterns = [
    path("index",views.index),
    path("<int:authors>",views.Authorss,name='auth-detail'),
    path("<str:slug_name>",views.slug,name='slug-detail'),
]
