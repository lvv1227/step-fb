from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpRequest,Http404

from .models import Question
from django.template import loader
from django.core.paginator import Paginator

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def post_list(request):
   # page = request.GET.get('page')
    #if page ==  None:
    #    raise Http404
    #print(page)
    #return HttpResponse('OK'+page)
    latest_question_list = Question.objects.order_by('-added_at')[:]

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'qa/index.html', context)



def post_list_all(request):
    questions = Question.objects.order_by('-added_at')
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page
    print(page.object_list)
    print(paginator.page_range)
    return render(request, 'qa/index2.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

def post_list_popular(request):
    questions = Question.objects.order_by('-rating')
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page) # Page
    print(page.object_list)
    print(paginator.page_range)
    return render(request, 'qa/index2.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()
    return render(request, 'qa/details.html', {'question': question,'answers':answers})
