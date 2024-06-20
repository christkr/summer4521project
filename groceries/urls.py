from django.urls import path
from . import views
from .views import custom_logout_view, home

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_items, name='search_items'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('allItems/', views.all_items, name='all_items'),
    path('accounts/logout/', custom_logout_view, name='logout')
]