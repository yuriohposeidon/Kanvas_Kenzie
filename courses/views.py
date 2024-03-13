from .models import Course
from .serializers import CourseSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class ListCreateCourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students = self.request.user)
        return Course.objects.all()

class RetrieveUpdateDeleteCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"