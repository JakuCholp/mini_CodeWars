from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Task, UserSolution, TestTask, UserTask
from .my_functions import create_function_string



@receiver(pre_save, sender=Task)
def add_first(sender, instance, **kwargs):
    new_first_text = create_function_string(instance.name_function, instance.count_arg)
    instance.first_text = 'def' + ' ' + new_first_text + '\n' + '   '
    



@receiver(post_save, sender=UserSolution)
def crt_task_user(sender, instance, **kwargs):
    if instance.count_succes == TestTask.objects.filter(task = instance.task).count():
        UserTask.objects.create(user=instance.user, task = instance.task, is_done = True)
    else:
        UserTask.objects.create(user=instance.user, task = instance.task, is_done = False)


