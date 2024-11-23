from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
class Student(models.Model):
    project_name = models.CharField(max_length=100)
    project_information = models.IntegerField()
    num_forms = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    college = models.CharField(max_length=30)
    student_id = models.CharField(max_length=11, unique=True)
    mobile = models.CharField(max_length=11, unique=True)


class Scholarship(models.Model):
    average_points = models.CharField(max_length=3)
    last_term_point = models.CharField(max_length=3)
    now_point = models.CharField(max_length=3)
    same_major_rank = models.IntegerField()

    number_students_same_major = models.IntegerField()
    poor_student = models.IntegerField()
    team_leader = models.IntegerField()
    prize = models.IntegerField()

class Upload(models.Model):
    file = models.FileField(upload_to='uploads/')
    choice = models.BooleanField(default=False)