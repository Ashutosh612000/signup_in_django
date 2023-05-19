from django.urls import path
from account.views import handleSignup,index,handlelogin,showusers,handlelogout

urlpatterns = [

    path('',index,name='index'),
    path('signup/',handleSignup,name='handleSignup'),
    path('login/',handlelogin,name='handlelogin'),
    path('showusers/',showusers,name='showusers'),
    path('logout/',handlelogout,name='handlelogout'),
]
