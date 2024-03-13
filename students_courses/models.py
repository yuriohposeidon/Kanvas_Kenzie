from django.db import models
from uuid import uuid4

class StudentCourseStatus(models.TextChoices):
    PEDING = "peding"
    ACCEPTED = "accepted"

class StudentCourse(models.Model):
    status = models.CharField(choices=StudentCourseStatus.choices, default=StudentCourseStatus.PEDING)
    course = models.ForeignKey("courses.Course", related_name= "students_courses", on_delete=models.CASCADE)    
    student = models.ForeignKey("accounts.Account", related_name= "students_courses", on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)