from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   
    path('',views.homepage,name='home-page'),
    path('login/',views.loginpage,name='login-page'),
    path('register/',views.registerpage,name='register-page'),
    path('profile/',views.profilepage,name='profile-page'),
    path('logout/',views.logoutpage,name='logout-page'),
    path('updateprofile/',views.updateprofilepage,name='updateprofile-page'),
  	path('deneme/',views.displaymessages,name='displaymessages-page'),
    path('search/',views.searchpage,name='search-page'),
	   path(r'profile/delete/<slug>/', views.confirmdeletepage, name='deletepost-page'),
    path(r'profile/<slug>/',views.userprofilepage,name='userprofile-page'),
    path(r'profile/addfriend/<slug>/',views.addfriendpage,name='addfriend-page'),
  
   
]
urlpatterns +=staticfiles_urlpatterns()
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 

