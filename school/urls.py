from school.views import Student, Teacher, Course


def register_api_urls(router):
    router.register(r'students', Student.StudentList)
    router.register(r'teachers', Teacher.TeacherList)
    router.register(r'courses', Course.CourseList)
