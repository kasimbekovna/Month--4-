from django.urls import path
from . import views

urlpatterns = [
    path("name/", views.name_view, name="hello"),
    path("hobby/", views.hobby_view, name="hobby"),
    path("", views.post_books_view, name="books"),
    path("books/<int:id>/", views.post_books_detail_view, name="books_detail"),
    path("book_list/", views.BookListView.as_view(), name="book_list"),
    path("book_list/<int:id>/", views.BookDetailView.as_view(), name="book_detail"),
    path(
        "book_list/<int:id>/delete/", views.DeleteBookView.as_view(), name="delete_book"
    ),
    path(
        "book_list/<int:id>/update/",
        views.UpdateBookView.as_view(),
        name="update_books",
    ),
    path("create_review/", views.CreatBookView.as_view(), name="create_review"),
    path("create_book/", views.CreatBookView.as_view(), name="create_book"),
    path("search/", views.SearchBookView.as_view(), name="search"),
]
