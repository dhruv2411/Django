from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def books(request):
    books = Book.objects.all().order_by('name')
    if request.GET.get('search'):
        books = books.filter(name__icontains = request.GET.get('search'))
        
    if request.GET.get('search_author'):
        books = books.filter(author__icontains = request.GET.get('search_author'))
    
    book_count = books.count()

    wishlist_books = WishlistBook.objects.all()
    wishlist_books_count = wishlist_books.count()

    current_books = CurrentBook.objects.all()
    current_books_count = current_books.count()

    context = {'books':books, 'book_count':book_count, 'wishlist_books_count':wishlist_books_count, 'current_books_count':current_books_count}
    return render(request, 'home.html',context)

def wishlist_books(request):
    wishlist_books = WishlistBook.objects.all().order_by('name')
    wishlist_books_count = wishlist_books.count()
    return render(request, 'wishlist.html',{'wishlist_books':wishlist_books, 'wishlist_books_count':wishlist_books_count})

def current_books(request):
    current_books = CurrentBook.objects.all().order_by('name')
    current_books_count = current_books.count()
    return render(request, 'currentbook.html',{'current_books':current_books,'current_books_count':current_books_count})

def add_books(request):
    if request.method == 'POST':
        book = request.POST

        book_name = book.get('book_name')
        book_author = book.get('book_author')
        book_learnings = book.get('book_learnings')
        book_genre = book.get('book_genre')

        Book.objects.create(
            name = book_name, 
            author = book_author, 
            learnings = book_learnings,
            genre = book_genre)
        return redirect('/')
    
    books = Book.objects.all()
    

    return render(request, 'addbook.html',{'books':books})

def delete_books(request, id):
    delete_books = Book.objects.get(id=id)
    if request.method == "POST":
        delete_books.delete()
        return redirect('/')
    
    return render(request, 'deletebook.html',{'delete_books':delete_books})


def change_books(request):
    change_books = Book.objects.all().order_by('name')
    return render(request, 'changebook.html',{'change_books':change_books})


def update_books(request, id):
    update_books = Book.objects.get(id=id)
    if request.method == "POST":
        book = request.POST

        book_name = book.get('book_name')
        book_author = book.get('book_author')
        book_learnings = book.get('book_learnings')
        book_genre = book.get('book_genre')

        update_books.name = book_name
        update_books.author = book_author
        update_books.learnings = book_learnings
        update_books.genre = book_genre

        update_books.save()
        return redirect('/')
    
    return render(request, 'updatebook.html',{'update_books':update_books})