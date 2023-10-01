from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')
def quiz(request):
    return render(request, 'quiz/quiz.html')
def login(request):
    return render(request, 'user/login.html')
def signup(request):
    return render(request, 'user/signup.html')