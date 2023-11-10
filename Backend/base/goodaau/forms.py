from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserDetail, BookSchedule

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border text-black '

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your username',
            'class':'w-full py-4 px-6 rounded-xl'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Your password',
            'class':'w-full py-4 px-6 rounded-xl'
        }
    ))

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your username',
            'class':'w-full py-4 px-6 rounded-xl'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Your email address',
            'class':'w-full py-4 px-6 rounded-xl'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Your password',
            'class':'w-full py-4 px-6 rounded-xl'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Re-type password',
            'class':'w-full py-4 px-6 rounded-xl'
        }
    ))

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('name','date_of_birth','father_name','citizenship_id','blood_group','address','phone_no','category','photo')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'date_of_birth': forms.DateInput(
                attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            ),
            'father_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'citizenship_id': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'blood_group': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'phone_no': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'photo': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = BookSchedule
        fields = ('pass_file','appointment_date')

        widgets = {
            'pass_file': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'appointment_date': forms.DateInput(
                attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            ),
        }