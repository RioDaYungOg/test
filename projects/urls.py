from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects,name='projects'),
    path('project/<str:pk>/',views.project,name='project')# pk для возможности project/1 project/2 etc....
]