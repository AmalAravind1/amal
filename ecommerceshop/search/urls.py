from django.urls import path
from . import views
app_name='search'
urlpatterns = [
 path('searchprod/',views.searchresult,name='searchresult'),
]


