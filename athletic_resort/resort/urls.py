"""athletic_resort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
from django.conf.urls import url
from resort import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^registration/', views.registration_view, name='registration'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^change_password/', views.change_password, name='change_password'),
    url(r'^room_list/', views.room_list, name='room_list'),
    url(r'^room_details/(?P<id>\d+)/(?P<room_type>[\w -:.%/]+)/$', views.room_details, name='room_details'),
    url(r'^note_pad', views.note_pad, name='note_pad'),
]
