from django.contrib import admin
from .models import *
# Register your models here.

class OptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'option')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question','ans')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(visitedQuestion)