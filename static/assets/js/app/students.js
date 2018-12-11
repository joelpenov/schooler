
(function () {

    function StudentModel(){
        var self = this;
        self.id = ko.observable();
        self.name = ko.observable();
        self.surname = ko.observable();
        self.birthDate = ko.observable("2004-12-07");

        self.update = function(data) {
            self.id(data.id);
            self.name(data.name);
            self.surname(data.surname);
            self.birthDate(data.birth_date);
            return self;
        }
    }

    function StudentViewModel(){
        var self = this;
        self.student = ko.observable(new StudentModel());
        self.students = ko.observableArray([]);
        
        self.loadStudents = function () {
            GSAX.get("/api/students/", function (data) {
                self.students(data.map(function(student){
                    return new StudentModel().update(student);
                }));
            })
        }

        self.getValidProperty=function(elementId, name, value, minLength){
            minLength = minLength || 2;
            if(!value || value.length < minLength){
                $("#" + elementId).notify(name + " es invalido");
                return null;
            }

            return value;
        }

        self.getStudentData = function(){
            var data = {
                name: self.getValidProperty("name", "Nombre", self.student().name()),
                surname:self.getValidProperty("surname", "Apellido", self.student().surname()),
                birth_date: self.getValidProperty("birthDate", "Fecha", self.student().birthDate())
            }

            if(!data.surname || !data.name || !data.birth_date) return;

            data.birth_date += "T00:00:00"

            return data;
        }

        self.addStudent = function() {

            var data = self.getStudentData();
             if(!data) return;
            GSAX.post("/api/students/", data, function (response) {
                self.student().update({});
                self.loadStudents();
            })
        }
    }

    $(document).ready(function () {
        var studentsViewModel = new StudentViewModel();
        ko.applyBindings(studentsViewModel, document.getElementById("students-view"));
        studentsViewModel.loadStudents();
    });

})();
