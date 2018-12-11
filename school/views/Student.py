from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import permissions, viewsets
from main.mixin import AtomicMixin
from school.models import Student
from school.serializers.Student import StudentSerializer


@login_required()
def students(request):
    return render(request, "students.html")


class StudentList(AtomicMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

