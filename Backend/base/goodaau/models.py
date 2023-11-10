from django.db import models
from django.contrib.auth.models import User
# Create your models here.

BLOOD_GROUP_CHOICE = [
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ("O+","O+"),
    ("O-","O-"),
    ("AB+","AB+"),
    ("AB-","AB-"),
]

CATEGORY_CHOICES = [
    ('A','A - Motorcycle, Scooter, Moped'),
    ('B','B - Car, Jeep, Delivery Van'),
    ('C','C - Tempo, Auto Rickshaw'),
    ('C1','C1 - E-Rickshaw'),
    ('D','D - Power Tiller'),
    ('E','E - Tractor'),
    ('F','F - Minibus, Minitruck'),
    ('G','G - Truck, Bus, Lorry'),
    ('H','H - Road Roller, Dozer'),
    ('K','K - Scooter, Moped'),
]

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=150, null= True, blank=True)
    date_of_birth = models.DateField(null=True , blank=True)
    father_name = models.CharField(max_length=150 , null=True, blank=True)
    citizenship_id = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.CharField(max_length=150, choices=BLOOD_GROUP_CHOICE, default="A+")
    address = models.CharField(max_length=150, null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="A" )
    photo = models.ImageField(default= "user_photo/avatar.svg", upload_to = "user_photo", null = True, blank = True)

    def __str__(self):
        return str(self.citizenship_id)
    

class Exam(models.Model):
    examiner = models.OneToOneField(UserDetail, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return str(self.examiner)
    

class BookSchedule(models.Model):
    user = models.OneToOneField(UserDetail,on_delete=models.CASCADE, null=True)
    pass_file = models.FileField(upload_to='pass_report')
    appointment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user.citizenship_id)
