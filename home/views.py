from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import books
from .forms import form_r

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
    return HttpResponse(template.render(context, request, ))

def get_radios(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form_r(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = form_r()

    return render(request, 'home/name.html', {'form': form})