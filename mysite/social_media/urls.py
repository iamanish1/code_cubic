from django.contrib import admin
from django.urls import path,include
from social_media import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('singup',views.singup,name="singup"),
    path('login',views.login,name="login"),
    path('communiity',views.communiity,name="communiity"),
    path('courses',views.courses,name="courses"),
    path('intern',views.intern,name="intern"),
    path('project',views.project,name="project")

]