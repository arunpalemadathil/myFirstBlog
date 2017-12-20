from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^morning/', views.morning, name='morning'),
    url(r'^article/(\d+)/', views.viewArticle, name='article'),
    url(r'^articles/(\d{2})/(\d{4})', views.viewArticles, name='articles'),
]
