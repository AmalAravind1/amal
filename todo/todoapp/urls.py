from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
path('cbvdetails/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetails'),
path('cbvupdates/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdates'),
path('cbvdelete/<int:pk>/',views.Deleteview.as_view(),name='cbvdelete')

]
