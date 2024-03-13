from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class Account(AbstractUser):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    my_courses = models.ManyToManyField("courses.Course", through="students_courses.StudentCourse", related_name="students")
