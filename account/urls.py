from django.urls import path
from account.views import handleSignup,index,handlelogin

urlpatterns = [

    path('',index,name='index'),
    path('signup/',handleSignup,name='handleSignup'),
    path('login/',handlelogin,name='handlelogin'),
]
