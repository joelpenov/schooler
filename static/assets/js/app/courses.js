
(function () {

    function StudentModel(){
        var self = this;
        self.id = ko.observable();
        self.name = ko.observable();
        self.wasAddedToThisCourse = ko.observable();

        self.update = function(data) {
            self.id(data.student_id);
            self.name(data.student_name);
            return self;
        }

        self.updateOriginal = function(data) {
            self.id(data.id);
            self.name(data.name + ' ' + data.surname);
            self.wasAddedToThisCourse(false);
            return self;
        }
    }

    function CourseModel(){
        var self = this;
        self.id = ko.observable();
        self.name = ko.observable();
        self.teacherName = ko.observable();
        self.teacherId = ko.observable();
        self.students = ko.observableArray([]);


        self.update = function(data) {
            self.id(data.id);
            self.name(data.name);
            self.teacherName(data.teacher_name);
            self.teacherId(data.teacher);
            self.students(data.students ? data.students.map(function(student){
                return new StudentModel().update(student)
            }) : []);

            return self;
        }
    }

    function CourseViewModel(){
        var self = this;
        self.course = ko.observable(new CourseModel());
        self.courses = ko.observableArray([]);
        self.teachers = ko.observableArray([]);
        self.students = ko.observableArray([]);
        self.studentsToShow = ko.observableArray([]);
        self.filterStudentCriterium = ko.observable();

        self.filterStudentCriterium.subscribe(function (newValue) {
            newValue = newValue || "";
            self.studentsToShow(self.students().filter(function (student) {
                return student.name().toLowerCase().indexOf(newValue.toLocaleString()) !== -1;
            }))
        });

        self.saveCourse = function(){
            var data = self.getCourseData();
            if(!data) return;

            GSAX.post("/api/courses/", data, function(response){
                self.loadCourses();
                self.course().update({});
                self.students().forEach(function (student) {
                    student.wasAddedToThisCourse(false);
                })
            })
        };

        self.loadCourses = function () {
            GSAX.get("/api/courses", function (data) {
                self.courses(data.map(function(course){
                    return new CourseModel().update(course);
                }));
            })
        }

        self.loadTeachers = function () {
            GSAX.get("/api/teachers", function (data) {
                data.forEach(function (teacher) {
                    teacher.name = teacher.name + ' ' + teacher.surname;
                })
                self.teachers(data);
            })
        }
        self.loadStudents = function () {
            GSAX.get("/api/students", function (data) {
                var models = data.map(function (student) {
                    return new StudentModel().updateOriginal(student)
                });
                self.students(models);
                self.studentsToShow(models);
            })
        }

        self.getCourseId = function(course){
            return "course_" + course.id();
        };

        self.deleteStudentFromCourse = function(student, b, d) {
            debugger;
        }

        self.getValidProperty=function(elementId, name, value, minLength){
            minLength = minLength || 2;
            if(!value || value.length < minLength){
                $("#" + elementId).notify(name + " es invalido");
                return null;
            }

            return value;
        }

        self.getCourseData = function(){

            var data = {
                name: self.getValidProperty("name", "Nombre del curso ", self.course().name()),
                teacher:self.getValidProperty("teacher", "Profesor seleccionado ", self.course().teacherId(), 0),
                students:[]
            }

            data.student_ids = self.students().filter(function (student) {
                return student.wasAddedToThisCourse() === true;
            }).map(function (student) {
                return student.id();
            })

            if(data.student_ids.length < 1){
                $("#studentsToShow").notify("Debe elegir al menos un estudiante");
                return;
            }

            return data;
        }

        self.addCourse = function() {

            var data = self.getCourseData();
             if(!data) return;
            GSAX.post("/api/courses/", data, function (response) {
                self.course().update({});
                self.loadCourses();
            })
        }
    }

    $(document).ready(function () {
        var coursesViewModel = new CourseViewModel();
        ko.applyBindings(coursesViewModel, document.getElementById("courses-view"));
        coursesViewModel.loadCourses();
        coursesViewModel.loadTeachers();
        coursesViewModel.loadStudents();
    });

})();
