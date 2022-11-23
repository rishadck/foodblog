from django .urls import path
from . import views
urlpatterns=[
    path('cartDeatails',views.cart_deatails,name='cartDeatails'),
    path('add/<int:product_id>/',views.add_cart,name="addcart"),
    path('decrement/<int:product_id>/',views.min,name="decrement"),
    path('remove/<int:product_id>/',views.cart_delete,name="remove"),
]