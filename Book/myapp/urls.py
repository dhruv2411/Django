from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name="books"),
    path('wishlist/', views.wishlist_books, name="wishlist_books"),
    path('currentbook/', views.current_books, name="current_books"),
    path('addbook/', views.add_books, name="add_books"),
    path('change_books/', views.change_books, name="change_books"),
    path('deletebook/<str:id>', views.delete_books, name="delete_books"),
    path('updatebook/<str:id>', views.update_books, name="update_books"),
]