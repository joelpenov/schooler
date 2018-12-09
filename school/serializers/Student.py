from rest_framework import serializers
from school.models import Student


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'name', "surname", "birth_date")
