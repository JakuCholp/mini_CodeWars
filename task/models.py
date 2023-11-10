from django.db import models
from user.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    name_function = models.CharField(max_length=159)
    count_arg = models.IntegerField()
    first_text = models.TextField(default=False)


class TestTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    test_var = models.TextField()
    result = models.TextField()



class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)



class UserSolution(models.Model):
    solution = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    count_succes = models.IntegerField()
    
