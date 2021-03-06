from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpRequest,Http404
from django.http import HttpResponseRedirect

from .models import Question
from .forms import AskForm,AnswerForm,SignupForm,SigninForm

from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login

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
    print(request.user)
    questions = Question.objects.order_by('-id')
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
    form = AnswerForm()
    return render(request, 'qa/details.html', {'question': question,
                                               'answers':answers,
                                               'question_id':question_id,
                                               'form':form})

def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user=request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            print(url)
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/question_add.html', {
        'form': form,

    })

def answer_add(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user=request.user
        if form.is_valid():
            answer = form.save()
            url = str(answer.question.id)
            url='/question/'+url+'/'
            print(url)
            return HttpResponseRedirect(url)

    return Http404

def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user = authenticate(username=form.get_username(), password=form.get_password())
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return Http404

    else: #GET, show the form
        form=SignupForm()
        return render(request, 'qa/signup.html', {
        'form': form,

        })

def signin(request):
    if request.method=="POST":
        form=SigninForm(request.POST)
        if form.is_valid():

            user = authenticate(username=form.get_username(), password=form.get_password())
            if user is None:
                return HttpResponse("Wrong username / password")
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return Http404

    else: #GET, show the form
        form=SigninForm()
        return render(request, 'qa/signin.html', {
        'form': form,

        })