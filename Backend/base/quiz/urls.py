from django.urls import path
from . import views
urlpatterns = [
    path('', views.exam, name='exam'),
    path('question/', views.question, name='question'),
    path('result/',views.result, name = "result"),
    path('fail/',views.failCodition, name = "fail"),
    path('schedule/',views.schedule, name = "schedule"),
    path('download/', views.pdf_report_create, name='download')
]
