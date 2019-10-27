from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.core.paginator import Paginator
from . import books
from .forms import form_r


@csrf_exempt
def get_books(request):
    # if this is a POST request we need to process the form data
    book_type = ""

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form_r(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if form.cleaned_data['choice_field'] == "1":
                book_type = "currently-reading"
                choice = "1"
            elif form.cleaned_data['choice_field'] == "2":
                book_type = "read"
                choice = "2"

    # if a GET (or any other method) we'll create a blank form
    else:
        choice = request.GET.get('choice')
        if choice:
            if str(choice) == "1":
                book_type = "currently-reading"
            else:
                book_type = "read"
        else:
            print("Choice doesn't exist ")
            choice = "1"
            book_type = "currently-reading"

    template = loader.get_template('home/reading.html')
    book_list = books.get_currentlyreading(book_type)
    paginator = Paginator(book_list, 3)
    page = request.GET.get('page')
    book_pages = paginator.get_page(page)

    form = form_r({'choice_field': str(choice)})
    context = {
        'book_list': book_pages,
        'form': form,
        'choice': choice
    }
    return HttpResponse(template.render(context, request))
