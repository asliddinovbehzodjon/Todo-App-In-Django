from django.urls import path

from .views import *

urlpatterns=[
path('',homepage),
path('register/',register,name='register'),
path('login/',loginPage,name='login'),
path('logout/',logoutUser,name='logout'),
path('update/<int:id>/',updatetodo),
path('delete/<int:id>/',deletetodo),
path('finish/<int:id>/',finishtodo),
path('continue/<int:id>/',davometish)


]
