# Generated by Django 4.2.7 on 2023-11-09 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersolution',
            old_name='couunt_succes',
            new_name='count_succes',
        ),
        migrations.AddField(
            model_name='usersolution',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
            preserve_default=False,
        ),
    ]