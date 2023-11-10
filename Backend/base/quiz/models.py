from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=250, null=True, blank=True)
    ans = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return str(self.id)

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    option = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.option

class visitedQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)