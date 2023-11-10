from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from .models import UserDetail, Exam
from .forms import SignupForm,ApplicationForm,ScheduleForm
import uuid

def home(request):
    if request.user.is_authenticated:
        template = "goodaau/home.html"
    else:   
        template = "goodaau/home_logout.html"

    return render(request,template)
 
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request,'goodaau/signup.html',{
        'form':form
    })

def application(request):
    if UserDetail.objects.filter(user = request.user):
        messages.error(request,"You have already submitted Application Form.!!")
        return redirect('home')
    else:
        if request.method == "POST":
            form = ApplicationForm(request.POST, request.FILES)

            if form.is_valid():
                apform = form.save(commit=False)
                apform.user = request.user
                apform.save()
                return redirect('payment')
        else:   
            form = ApplicationForm()
        
    return render(request,'goodaau/applicationForm.html',{"form":form})

def userProfile(request):
    return render(request,'goodaau/user_profile.html')

def userDetailEdit(request):
    user = UserDetail.objects.get(user = request.user)
    form = ApplicationForm(instance=user)
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES, instance=user )
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile was updated")
            return redirect('profile')
    return render(request,'goodaau/applicationForm.html',{'form':form})

def paypal_payment(request):
    user = UserDetail.objects.get(user = request.user)
    exam = Exam.objects.filter(examiner = user)
    if exam:
        return redirect('home')
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '1500.00',
        'item_name':'Payment for Exam',
        'invoice': str(uuid.uuid4()),
        'currency_code':'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f'http://{host}{reverse("payment_done")}',
        'cancel_return': f'http://{host}{reverse("payment_cancelled")}',
    }
    form = PayPalPaymentsForm(initial = paypal_dict)

    context = {'form':form}
    return render(request, 'goodaau/payment.html',context)

def payment_done(request):
    user = UserDetail.objects.get(user = request.user)

    Exam.objects.create(
        examiner = user,
        status = False
    )

    messages.success(request,f"You've successfully made a payment! Now you are eligible to give exam within 1 month!!")
    return redirect('home')

def payment_cancelled(request):
    messages.error(request,"You've cancelled your payment")
    return redirect('home')

