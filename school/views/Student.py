from rest_framework import permissions, viewsets
from main.mixin import AtomicMixin
from school.models import Student
from school.serializers.Student import StudentSerializer


class StudentList(AtomicMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

