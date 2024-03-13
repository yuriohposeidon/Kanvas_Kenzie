from .models import Content
from .serializers import ContentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from courses.models import Course
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsAdminOrStudent


class ListCreateContentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not course:
            raise NotFound({"detail": "course not found."})
        serializer.save(course=course)

class RetrieveUpdateDeleteContentView(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrStudent ]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_object(self):
        try:
            Course.objects.get(pk=self.kwargs["course_id"])
            content = Content.objects.get(pk=self.kwargs["content_id"])
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        self.check_object_permissions(self.request, content)
        return content