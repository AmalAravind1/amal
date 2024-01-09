from django.urls import path
from . import views
app_name='cartappp'
urlpatterns=[
    path('add/<int:product_id>/',views.cart_add,name='cart_add'),
    path('details/',views.cart_details,name='cartdetails'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/',views.cart_delete,name='cart_delete'),
]