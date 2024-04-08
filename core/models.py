from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128)


class Module(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')



class Tutor(models.Model):
    name = models.CharField(max_length=128)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='tutors')