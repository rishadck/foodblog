from django . urls import path
from .  import views

urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:cr_slug>/',views.home,name='prod_cat'),
    path('<slug:cr_slug>/<slug:product_slug>',views.prodectdetails,name='details'),
    path('search',views.search,name="search")
 
]