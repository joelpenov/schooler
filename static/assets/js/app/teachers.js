
(function () {

    function TeacherModel(){
        var self = this;
        self.id = ko.observable();
        self.name = ko.observable();
        self.surname = ko.observable();
        self.username = ko.observable();

        self.update = function(data) {
            self.id(data.id);
            self.name(data.name);
            self.surname(data.surname);
            self.username(data.username);
            return self;
        }
    }

    function TeacherViewModel(){
        var self = this;
        self.teacher = ko.observable(new TeacherModel());
        self.teachers = ko.observableArray([]);

        self.loadTeachers = function () {
            GSAX.get("/api/teachers/", function (data) {
                self.teachers(data.map(function(teacher){
                    return new TeacherModel().update(teacher);
                }));
            })
        }

        self.username = ko.computed(function () {

            if(!self.teacher().surname() || !self.teacher().name()) return;

             return self.teacher().surname().indexOf(" ") === -1 ? self.teacher().name()[0].toLowerCase() + self.teacher().surname().toLowerCase() :
                self.teacher().name()[0].toLowerCase() + self.teacher().surname().substring(0,self.teacher().surname().indexOf(" ")).toLowerCase();
        });

        self.getValidProperty=function(elementId, name, value, minLength){
            minLength = minLength || 2;
            if(!value || value.length < minLength){
                $("#" + elementId).notify(name + " es invalido");
                return null;
            }

            return value;
        }

        self.getTeacherData = function(){
            var data = {
                name: self.getValidProperty("name", "Nombre", self.teacher().name()),
                surname:self.getValidProperty("surname", "Apellido", self.teacher().surname())
            }

            if(!data.surname || !data.name) return;

            return data;
        }

        self.addTeacher = function() {

            var data = self.getTeacherData();
            data.username = self.username();

            if(!data) return;

            GSAX.post("/api/teachers/", data, function (response) {
                self.teacher().update({});
                self.loadTeachers();
            })
        }
    }

    $(document).ready(function () {
        var teachersViewModel = new TeacherViewModel();
        ko.applyBindings(teachersViewModel, document.getElementById("teachers-view"));
        teachersViewModel.loadTeachers();
    });

})();
