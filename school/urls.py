from school.views import Student, Teacher, Course
from django.conf.urls import url


def register_api_urls(router):
    router.register(r'students', Student.StudentList)
    router.register(r'teachers', Teacher.TeacherList)
    router.register(r'courses', Course.CourseList)


urlpatterns = [
    url(r'^students/', Student.students),
    url(r'^teachers/', Teacher.teachers),
]
