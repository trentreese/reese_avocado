from django.http import HttpResponse
from django.template import loader
from . import books
from .forms import NameForm

def index(request):
    template = loader.get_template('home/index.html')
    book_type = ""
    some_var = request.POST.getlist('checks')
    print(some_var)
    if some_var == "id_cr":
        # Checkbox was selected
        book_type = "currently-reading"
    elif 'reading' in request.GET:
        book_type = "read"
    else:
        book_type = ""
        

    book_list = books.get_currentlyreading(book_type)
    context = {
        'book_list': book_list
    }
    return HttpResponse(template.render(context, request))