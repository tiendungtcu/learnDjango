from django.urls import path, re_path
from tutorials import views 
 
urlpatterns = [ 
    re_path(r'^tutorials$', views.tutorial_list),
    re_path(r'^tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path(r'^tutorials/published$', views.tutorial_list_published)
]