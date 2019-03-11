from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.user_page,name = 'user_page'),
    url(r'^search/', views.search_result, name='search_result'),
