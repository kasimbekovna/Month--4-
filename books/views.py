from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic


# Update
class UpdateBookView(generic.UpdateView):
    template_name = "books/edit.html"
    form_class = forms.BookForm
    success_url = "/book_list/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.MyBook, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBookView, self).form_valid(form=form)


# DELETE
class DeleteBookView(generic.DeleteView):
    template_name = "books/confirm_delete.html"
    success_url = "/book_list/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.MyBook, id=book_id)


# CREATE
class CreatBookView(generic.CreateView):
    template_name = "books/create_book.html"
    form_class = forms.BookForm
    success_url = "/book_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatBookView, self).form_valid(form=form)


# список книг
class BookListView(generic.ListView):
    template_name = "books/book_list.html"
    context_object_name = "books"
    model = models.MyBook

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


# Детальная информация о телефонах
class BookDetailView(generic.DetailView):
    template_name = "books/book_detail.html"
    context_object_name = "book_id"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.MyBook, id=book_id)


class SearchBookView(generic.ListView):
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 5

    def get_queryset(self):
        return models.MyBook.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["q"] = self.request.GET.get("q")
        return contex


# class PostBooksView(generic.ListView):
#     model = models.MyBook
#     template_name = 'post_books.html'
#     context_object_name = 'posts'
#     ordering = ['-id']
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['video_content'] = models.VideoContent.objects.order_by('-id')
#         return context


# 2-не полная информация
def post_books_view(request):
    if request.method == "GET":
        posts = models.Books.objects.filter().order_by("-id")
        video_content = models.VideoContent.objects.filter().order_by("-id")
        return render(
            request,
            template_name="post_books.html",
            context={"posts": posts, "video_content": video_content},
        )


# 2 подробная информация при клике на кнопку подробнее
def post_books_detail_view(request, id):
    if request.method == "GET":
        post_id = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name="post_books_detail.html",
            context={"post_id": post_id},
        )


def name_view(request):
    if request.method == "GET":
        return HttpResponse("Исмаилова Самара")


def hobby_view(request):
    if request.method == "GET":
        return HttpResponse("волейбол")
