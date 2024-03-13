from django.db import models
from uuid import uuid4
class CourseStatus(models.TextChoices):
    NOTSTARTED = "not started"
    INPROGRESS = "in progress"
    FINISHED = "finished"

class Course(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length= 11,choices=CourseStatus.choices, default=CourseStatus.NOTSTARTED)
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey("accounts.Account", related_name= "courses", on_delete=models.PROTECT, null=True)