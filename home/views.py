from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from . import books
from .forms import form_r


@csrf_exempt
def get_books(request):
    # if this is a POST request we need to process the form data
    book_type = ""
    default_choice = "1"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form_r(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            default_choice = form.cleaned_data['choice_field']
            if form.cleaned_data['choice_field'] == "1":
                book_type = "currently-reading"
            elif form.cleaned_data['choice_field'] == "2":
                book_type = "read"

    # if a GET (or any other method) we'll create a blank form
    else:
        book_type = "currently-reading"

    template = loader.get_template('home/reading.html')
    book_list = books.get_currentlyreading(book_type)
    form = form_r({'choice_field': default_choice})
    context = {
        'book_list': book_list,
        'form': form
    }
    return HttpResponse(template.render(context, request))
