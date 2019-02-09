from django.http import HttpResponse
from django.template import loader


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('home/index.html')
    context = {
        'latest_question_list': 1,
    }
    return HttpResponse(template.render(context, request))