from rest_framework import viewsets, permissions
from main.mixin import AtomicMixin
from school.models import Course
from school.serializers.Course import CourseSerializer


class CourseList(AtomicMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_fields = ('teacher', 'id')
