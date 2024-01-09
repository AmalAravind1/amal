
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
   path('movies/<int:movies_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
