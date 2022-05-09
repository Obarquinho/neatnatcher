from django.shortcuts import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    # can do return render(request, 'polls/index.html', context)
    # instead 

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        #can also be
        #question = get_object_or_404(Question, pk=question_id)
        #does not need try/except body because it will just render whatever is returned
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)