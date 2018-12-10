from rest_framework import serializers
from school.models import Course, CourseStudent, Student


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
        fields = ('id', "name", "teacher_name", "teacher", "students")

    @staticmethod
    def get_teacher_name(obj):
        return obj.teacher.name + " " + obj.teacher.surname

    def create(self, validated_data):

        student_ids = self.context["request"].data["student_ids"]

        if len(student_ids) == 0:
            raise serializers.ValidationError("El curso debe tener al menos un estudiante")

        validated_data.pop("students")

        course = Course.objects.create(**validated_data)
        course.save()

        self.update_course_students(course, student_ids)

        return course

    @staticmethod
    def update_course_students(course, student_ids):

        for student in course.students.all():
            student.delete()

        students = Student.objects.filter(pk__in=student_ids)

        for student in students:
            CourseStudent.objects.create(course=course, student=student)



