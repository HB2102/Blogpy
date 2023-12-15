from django.template.defaulttags import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.IndexPage.as_view(), name='index'),
    path(r'contact/', views.ContactPage.as_view(), name='contact'),

    path(r'article/', views.SingleArticleAPIView.as_view(), name='single_article'),
    path(r'article/all/', views.AllArticleAPIView.as_view(), name='all_articles'),
    path(r'article/search/', views.SearchArticleAPIView.as_view(), name='search_articles'),
    path(r'article/submit/', views.SubmitArticleAPIView.as_view(), name='submit_articles'),
]