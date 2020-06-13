from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.homepage , name='homepage' ),
    path('login/', views.loginpage ,name='login'),
    path('login/teacher/addstudent', views.addstudent, name= 'addstd'),
    path('login/teacher/', views.seedetails, name= 'seedetails'),
    path('query/', views.raisequery, name ='raisequery'),
    # path('studentdata',views.studentdata, name= 'studentdata'),

    path('seequery/',views.seequery,name='seequery'),
    path('updatequery/',views.updatequery, name='updatequery'),
    path('image/', views.inserting , name='inserting')
]
