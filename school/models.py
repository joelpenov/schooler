from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=180)
    surname = models.CharField(max_length=180)
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=180)
    surname = models.CharField(max_length=180)
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=180)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.name


class CourseStudent(models.Model):
    course = models.ForeignKey(Course, related_name="students", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="courses", on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name + ' ' + self.student.name
