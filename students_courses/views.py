from .models import StudentCourse
from .serializers import StudentCourse
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class RetrieveUpdateStudentCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourse