from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    # path(r'^view/(?P<username>\w+)/$', views.index, name='index'),
    # path('view', views.index, name='index'),
    path('search/', views.searchPosts, name='search'),
    path('view/', views.viewPosts, name='view'),
    # re_path(r'^view/(?:order-(?P<orderby>\d+)/)?$', views.index, name='view'),
    # re_path(r'^comments/(?:page-(?P<page_number>\d+)/)//(?:page2-(?P<page_number>\d+)/)?$', views.searchFunction, name='search'),
        # /(?:query-(?P<searchQuery>\d+)/)'
    
]
