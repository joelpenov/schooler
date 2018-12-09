from rest_framework import serializers
from school.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Teacher
        fields = ('id', 'name', "surname", "username")

