from django.shortcuts import render
from .models import Quiz, QuizClass
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def qpage(request, slug):
    quizclass = QuizClass.objects.get(slug = slug)
    question = Quiz.objects.all()
    return render(request, 'quiz/quiz.html', {'Questions': question, 'QuizClass': quizclass})