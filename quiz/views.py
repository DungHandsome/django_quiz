from django.shortcuts import render
from .models import Quiz
# Create your views here.

def qpage(request):
    question = Quiz.objects.all()
    return render(request, 'quiz/quiz.html', {'Questions': question})