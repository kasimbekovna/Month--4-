from django.urls import path
from .views import (name_view, hobby_view, post_books_view,
                    post_books_detail_view, book_list, book_detail)
from . import views

urlpatterns = [
    path('name/', name_view, name='hello'),
    path('hobby/', hobby_view, name='hobby'),
    path('books/', post_books_view, name='books'),
    path('books/<int:id>/', post_books_detail_view, name='books_detail'),
    path('book_list/', book_list, name='book_list'),
    path('book_list/<int:id>/', book_detail, name='book_detail'),
    path('book_list/<int:id>/delete/', views.delete_book_view, name='delete_book'),
    path('book_list/<int:id>/update/', views.update_book_view, name='update_books'),
    path('create_review/', views.create_review_view, name='create_review')
]