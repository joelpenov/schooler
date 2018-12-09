from rest_framework import permissions, viewsets
from main.mixin import AtomicMixin
from school.models import Teacher
from school.serializers.Teacher import TeacherSerializer


class TeacherList(AtomicMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

