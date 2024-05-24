from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic



# Update
class UpdateBookView(generic.UpdateView):
    template_name = 'books/edit.html'
    form_class = forms.BookForm
    success_url = '/book_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.MyBook, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBookView, self).form_valid(form=form)


# DELETE
class DeleteBookView(generic.DeleteView):
    template_name = 'books/confirm_delete.html'
    success_url = '/book_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.MyBook, id=book_id)


# CREATE
class CreatBookView(generic.CreateView):
    template_name = 'books/create_book.html'
    form_class = forms.BookForm
    success_url = '/book_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatBookView, self).form_valid(form=form)


# список книг
class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    model = models.MyBook

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


# Детальная информация о телефонах
class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.MyBook, id=book_id)


class SearchBookView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return models.MyBook.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['q'] = self.request.GET.get('q')
        return contex


# def update_book_view(request, id):
#     book_id = get_object_or_404(models.MyBook, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Book edited!</h3>')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, template_name='books/edit.html',
#                   context={'book_id': book_id, 'form': form})


# def delete_book_view(request, id):
#     book_id = get_object_or_404(models.MyBook, id=id)
#     book_id.delete()
#     return HttpResponse("deleted")

# def create_review_view(request):
#     if request.method == 'POST':
#         form = forms.ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Your review has been created!</h1>')
#     else:
#         form = forms.ReviewForm()
#
#     return render(request, template_name='books/create_review.html',
#                   context={'form': form})


# def book_list(request):
#     if request.method == 'GET':
#         books = models.MyBook.objects.filter().order_by('-id')
#         return render(request, template_name='books/book_list.html',
#                       context={'books': books})


# def book_detail(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.MyBook, id=id)
#         return render(request, template_name='books/book_detail.html',
#                       context={'book_id': book_id})



# 2-не польная информация
def post_books_view(request):
    if request.method == 'GET':
        posts = models.Books.objects.filter().order_by('-id')
        return render(request, template_name='post_books.html',
                      context={'posts': posts})


# 2 подробная информация при клике на кнопку подробнее
def post_books_detail_view(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(models.Books, id=id)
        return render(request, template_name='post_books_detail.html',
                      context={'post_id': post_id})




def name_view(request):
    if request.method == 'GET':
        return HttpResponse('Исмаилова Самара')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('волейбол')


