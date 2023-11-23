from django.template.defaulttags import url
from django.urls import path
# from django.conf.urls impo
from . import views

urlpatterns = [
    path(r'', views.IndexPage.as_view(), name='index'),
    path(r'contact/', views.ContactPage.as_view(), name='contact'),

    path(r'article/all/', views.AllArticleAPIView.as_view(),name='all_articles'),
]