from django.contrib import admin
from .models import Task, TestTask, UserSolution, UserTask

# Register your models here.
admin.site.register(Task)
admin.site.register(TestTask)
admin.site.register(UserSolution)
admin.site.register(UserTask)

