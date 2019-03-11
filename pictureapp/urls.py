from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.user_page,name = 'user_page'),
    url(r'^search/', views.search_result, name='search_result'),
        url(r'^user/(\d+)', views.single_user, name='single_user'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^post/', views.post, name='post'),
