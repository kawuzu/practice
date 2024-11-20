from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic
# Create your views here.

def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_genres=Genre.objects.all().count()
    num_incl=Book.objects.filter(title__icontains='whispers').count()
    num_languages=Language.objects.all().count()

    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_visits = request.session.get('num_visits', 0)

    request.session['num_visits'] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,
                 'num_authors':num_authors, 'num_genres':num_genres, 'num_incl':num_incl, 'num_languages':num_languages,
                 'num_visits':num_visits},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
class AuthorDetailView(generic.DetailView):
    model = Author
