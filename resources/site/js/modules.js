$(document).ready(function() {
    var callbackModulesGroup = function (data, status){
        if(data){
            var group_options = '';

            data.forEach(function(group){
                group_options += '<option value="'+ group.code +'">'+ group.name +'</option>';
            });

            $("#group").html(group_options);
        }
        
    }

    var data = {
        "classname": "login.getGroupModules",
        "name": ""
    }

    sugelico.getServerCall(data, callbackModulesGroup);

    // GET ALL MODULES
    var getAllModulesCallback = function(data, status) {
        var currentTable;
        console.log(data);
        var editDeleteBtnTemplate = '<button class="btn btn-success edit_module left" data-id="\{id\}" ' +
            'data-toggle="modal" data-target="#edit_module"><i class="fa fa-pencil"></i></button>' +
                                    '<button class="btn btn-default delete_module" data-id="\{id\}" ' +
            'data-toggle="modal" data-target="#delete_module"><i class="fa fa-remove"></i></button>';
        
        if ($('#modules_table').val() == "") {
            currentTable = $('#modules_table').DataTable();
        }

        data.forEach(function(module){
            currentTable.row.add([
                module.code,
                module.name,
                module.path,
                module.icon,
                module.group,
                editDeleteBtnTemplate.replace("\{id\}", module.code).replace("\{id\}", module.code)
            ]).draw( false );
        });

        $('#modules_table tbody').on('click', 'button.edit_module', function () {
            editModuleBtnClicked($(this));
        });

        $('#modules_table tbody').on('click', 'button.delete_module', function () {
            deleteModuleBtnClicked($(this));
        } );
    }

    var data = {
        "classname": "login.getModules",
        "name": ""
    }

    sugelico.getServerCall(data, getAllModulesCallback);


    // ADD MODULE
    $("#add_module").click(function(event){
        event.preventDefault();
        $(this).prop( "disabled", true );
        var data = {
            "classname": "login.HandleModule",
            "name": $("#name").val(),
            "path": $("#path").val(),
            "icon": $("#icon").val(),
            "group": $("#group").val().join("|")
        }

        var addModuleCallback = function(data, status){
            if (data.code) {
                $("#add_module_form").find("input").val('');
                $("#add_module_form").find("select").val('').trigger("change");
                $("#error_alert").addClass("hidden");
                $("#success_alert").removeClass("hidden");
                $("#add_module").prop( "disabled", false);
            } else {
                $("#error_alert").removeClass("hidden");
                $("#success_alert").addClass("hidden");
            }

            $( this).prop( "disabled", false );
        }

        sugelico.postServerCall(data, addModuleCallback);
    });


	// EDIT MODULE
    var editModuleBtnClicked = function(currentModule){
        var editModuleModal = $("#edit_module");
        editModuleModal.data("id", currentModule.data("id"))

        var callback = function (data, status) {
            var module = data[0];
            editModuleModal.find("#module_name").val(module.name);
            editModuleModal.find("#icon").val(module.icon);
            editModuleModal.find("#path").val(module.path);
            editModuleModal.find("#group").val(module.group).trigger("change");
        }

        var data = {
            "classname": "login.getModules",
            "name": "",
            "code": currentModule.data("id")
        }
        console.log(data);

        sugelico.getServerCall(data, callback);

        var editModuleCallback = function(data, status){
            console.log(data);
            if (data.code) {
                window.location.reload();
            }
        }

        $("#edit_module_btn").click(function(){
            var form = editModuleModal.find("#edit_module_form");
            var data = {
                "classname": "login.HandleModule",
                "code": editModuleModal.data("id"),
                "icon": editModuleModal.find("#icon").val(),
                "path": editModuleModal.find("#path").val(),
                "group": editModuleModal.find("#group").val().join("|"),
                "name": editModuleModal.find("#module_name").val()
            }
            sugelico.postServerCall(data, editModuleCallback);
        });
    }

    var deleteModuleBtnClicked = function (currentModule) {
        var deleteModuleModal = $("#delete_module");

        var deleteModuleCallback = function(data, status){
            console.log(data);
        }

        $("#delete_module_btn").click(function(){
            deleteModuleModal.modal("hide");
            var data = {
                "classname":"login.HandleModule",
                "status":13, 
                "name": "",
                "code": currentModule.data("id")
            }
            sugelico.postServerCall(data, deleteModuleCallback);
        });
    }

});