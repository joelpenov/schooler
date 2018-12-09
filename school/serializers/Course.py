from rest_framework import serializers
from school.models import Course


class CourseStudentsSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    student_id = serializers.SerializerMethodField()

    @staticmethod
    def get_student_name(obj):
        return obj.student.name + " " + obj.student.surname

    @staticmethod
    def get_student_id(obj):
        return obj.student.id

    class Meta:
        model = Course
        fields = ('student_id', "student_name")


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    students = CourseStudentsSerializer(many=True, required=True)
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'name', "teacher_name","teacher", "students")

    @staticmethod
    def get_teacher_name(obj):
        return obj.teacher.name + " " + obj.teacher.surname

