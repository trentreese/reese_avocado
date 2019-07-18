from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import books
from .forms import NameForm

@csrf_exempt 
def index(request):
    template = loader.get_template('home/index.html')
    book_type = ""
    if request.POST.get('radios')== "id_cr":
        print("cr")
        book_type = "currently-reading"
    elif request.POST.get('radios') == "id_r":
        print("r")
        book_type = "read"
    else:
        print("other")
        book_type = "currently-reading" # default to currently-reading on page load

    book_list = books.get_currentlyreading(book_type)
    context = {
        'book_list': book_list
    }
    return HttpResponse(template.render(context, request))