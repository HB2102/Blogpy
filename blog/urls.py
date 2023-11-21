from django.urls import path
# from django.conf.urls impo
from . import views

urlpatterns = [
    path(r'', views.IndexPage.as_view(), name='index'),
    path(r'contact/', views.ContactPage.as_view(), name='contact'),
]