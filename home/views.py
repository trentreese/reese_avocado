from django.http import HttpResponse
from django.template import loader
from . import books

def index(request):
    template = loader.get_template('home/index.html')
    book_list = books.get_currentlyreading()
    context = {
        'book_list': book_list
    }
    return HttpResponse(template.render(context, request))