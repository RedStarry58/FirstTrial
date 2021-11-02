from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='LogService:login')
def index(request):
    question_list = Question.objects.order_by('-create_date')
    page = request.GET.get('page', '1')

    paginator = Paginator(question_list, 5)  # 페이지당5개씩보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'App_Board/question_list.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('App_Board:detail', question_id=question.id)
    else:
        form = AnswerForm()

    context = {'question': question, 'form': form}
    return render(request, 'App_Board/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('App_Board:detail', question_id=question.id)
    else:
        form = AnswerForm()

    context = {'question': question, 'form': form}
    return render(request, 'App_Board/question_detail.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('App_Board:index')
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'App_Board/question_form.html', context)
