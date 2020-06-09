from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.homepage , name='homepage' ),
    path('login/', views.loginpage ,name='login'),
    path('login/teacher/addstudent', views.addstudent, name= 'addstd'),
    path('login/teacher/', views.seedetails, name= 'seedetails')
]
