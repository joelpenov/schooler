from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import permissions, viewsets
from main.mixin import AtomicMixin
from school.models import Teacher
from school.serializers.Teacher import TeacherSerializer


@login_required()
def teachers(request):
    return render(request, "teachers.html")


class TeacherList(AtomicMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

