from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


def update_book_view(request, id):
    book_id = get_object_or_404(models.MyBook, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Book edited!</h3>')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='books/edit.html',
                  context={'book_id': book_id, 'form': form})


def delete_book_view(request, id):
    book_id = get_object_or_404(models.MyBook, id=id)
    book_id.delete()
    return HttpResponse("deleted")


def create_review_view(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Your review has been created!</h1>')
    else:
        form = forms.ReviewForm()

    return render(request, template_name='books/create_review.html',
                  context={'form': form})



def book_list(request):
    if request.method == 'GET':
        books = models.MyBook.objects.filter().order_by('-id')
        return render(request, template_name='books/book_list.html',
                      context={'books': books})

def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.MyBook, id=id)
        return render(request, template_name='books/book_detail.html',
                      context={'book_id': book_id})



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


