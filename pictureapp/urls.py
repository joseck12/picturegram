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
    url(r'^comment/(\d+)', views.comment, name='comment'),
    url(r'^test/', views.test, name='test'),
    url(r'^update/profile', views.update_profile, name='update_profile'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^more/(\d+)', views.more, name='more'),
    url(r'^view/profiles', views.view_profiles, name='viewProfiles'),
    url(r'^follow/(\d+)',views.follow ,name='follow'),
    url(r'^like/(\d+)',views.like ,name='like')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
