from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets, permissions
from main.mixin import AtomicMixin
from school.models import Course
from school.serializers.Course import CourseSerializer


@login_required()
def courses(request):
    return render(request, "courses.html")


class CourseList(AtomicMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_fields = ('teacher', 'id')

