from django.urls import path
from . import views
from contents.views import ListCreateContentView, RetrieveUpdateDeleteContentView
from students_courses.views import RetrieveUpdateStudentCourseView
urlpatterns = [
    path("courses/", views.ListCreateCourseView.as_view(),
         ),
    path("courses/<uuid:course_id>/", views.RetrieveUpdateDeleteCourseView.as_view(),
         ),
    path("courses/<uuid:course_id>/contents/", ListCreateContentView.as_view()),

    path("courses/<uuid:course_id>/contents/<uuid:content_id>/", RetrieveUpdateDeleteContentView.as_view()),

    path ("courses/<uuid:course_id>/students/", RetrieveUpdateStudentCourseView.as_view()),
    
]