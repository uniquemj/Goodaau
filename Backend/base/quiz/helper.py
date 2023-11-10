from .models import Question, Option, visitedQuestion
import random
from django.shortcuts import render,redirect
from goodaau.models import UserDetail, Exam

def verifyQuestion():
    i = random.randint(1,12)
    ques = Question.objects.get(id = i)
    totalVisit = visitedQuestion.objects.all().count()
    if totalVisit < 10:
        try: 
            visit = visitedQuestion.objects.get(question = ques, status = True)
            if visit: 
                return verifyQuestion()

        except visitedQuestion.DoesNotExist:
            visitedQuestion.objects.create(question = ques, status = True)
            
            return ques
    else:
        return None
    
def CalculateMarks(questionAns, choiceAnswer, user):
    userDetail = UserDetail.objects.get(user = user)
    examinee = Exam.objects.get(examiner = userDetail)

    print(questionAns == choiceAnswer)

    if choiceAnswer is not None and str(questionAns) == str(choiceAnswer):
        examinee.marks += 10
        print(examinee.marks)
        examinee.save()
            