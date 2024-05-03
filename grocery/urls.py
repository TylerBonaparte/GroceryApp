from django.urls import path
from . import views

app_name = 'grocery'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('list/', views.list_items, name='list_items'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('categories/', views.categories, name='categories'),  
    path('about_us/', views.about_us, name='about_us'),        
    path('contact/', views.contact, name='contact'),           
    path('cart/', views.cart, name='cart'),                  
]
