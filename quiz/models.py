from django.db import models

# Create your models here.
class QuizClass(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)


class Quiz(models.Model):
    quizclass = models.ForeignKey(QuizClass, related_name='question', on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)