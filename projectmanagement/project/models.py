from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=10)
    user_birthday = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

class Project(models.Model):
    user_id = models.ForeignKey(User,\
        related_name='project', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=10)
    total_budget = models.IntegerField()
    deadline = models.CharField(max_length=10)

    def __str__(self):
        return self.project_name

class Income(models.Model):
    project_id = models.ForeignKey(Project,\
        related_name='project_income', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, \
        related_name='user_income', on_delete=models.CASCADE)
    income = models.IntegerField()
    date = models.CharField(max_length=10)
