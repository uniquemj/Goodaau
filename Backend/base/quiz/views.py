from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from goodaau.forms import ScheduleForm
from goodaau.models import Exam,UserDetail
from .models import Question, Option, visitedQuestion
from .helper import CalculateMarks,verifyQuestion
import random
from xhtml2pdf import pisa
from django.template.loader import get_template
import datetime


def exam(request):
    question = Question.objects.get(id = 1)
    return render(request,'quiz/exam.html', {'question':question})

def question(request):
    questi= verifyQuestion()
    if questi is None:
        return redirect('result')
    
    currVisit = visitedQuestion.objects.get(question = questi)

    previd = currVisit.id if visitedQuestion.objects.all().count() <=1 or visitedQuestion.objects.all().count() > 10 else currVisit.id - 1

    prevQuestion = visitedQuestion.objects.get(id = previd)

    user = request.user
    chooseAns = str(request.POST.get('btn'))

    if chooseAns is not None:
        CalculateMarks(prevQuestion.question.ans, chooseAns, user)


    qna = Question.objects.get(id = questi.id)
    option = Option.objects.filter(question= qna)

    context = {
        'questions': questi,
        'option':option
    }
    return render(request,'quiz/question.html',context)

def result(request):
    visit = visitedQuestion.objects.all()
    visit.delete()

    userDetail = UserDetail.objects.get(user = request.user)
    examinee = Exam.objects.get(examiner = userDetail)
    print(examinee.status)
    if examinee.marks > 20:
        examinee.status = True
        examinee.save()
    
    context = {
        'passStatus': examinee.status
    }
    return render(request, 'quiz/result.html',context)

def failCodition(request):
    userDetail = UserDetail.objects.get(user = request.user)
    examinee = Exam.objects.get(examiner = userDetail)
    examinee.delete()
    userDetail.delete()
    return redirect('home')

def pdf_report_create(request):
    userDetail = UserDetail.objects.get(user = request.user)
    template_path = 'quiz/report.html'
    curr_datetime = datetime.datetime.now()
    curr_date = curr_datetime.date()

    context = {
        'user':userDetail,
        'issued_date': curr_date
    }
    
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = f'filename="ValidPassreport-{request.user.userdetail.citizenship_id}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def schedule(request):
    if request.method == "POST":
            form = ScheduleForm(request.POST, request.FILES)

            if form.is_valid():
                scheduleform = form.save(commit=False)
                user = UserDetail.objects.get(user = request.user)
                scheduleform.user = user
                scheduleform.save()
                messages.success(request, "You have booked your trial day!! Make sure to bring pass pdf along with you !!")
                return redirect('home')
    else:   
        form = ScheduleForm()
    
    context = {'form': form}
    return render(request,'goodaau/schedule.html',context)