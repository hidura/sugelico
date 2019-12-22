$(document).ready(function() {

    //LOAD all Users
    var getUserCallBack = function (data, status) {
        if(data){
            var currentTable;
            var editDeleteBtnTemplate = '<button class="btn btn-success edit_user left" data-id="\{id\}"' +
                ' data-toggle="modal" data-target="#edit_user"><i class="fa fa-pencil"></i></button>' +

                '<button class="btn btn-default delete_user" data-id="\{id\}" data-toggle="modal" ' +
                'data-target="#delete_user"><i class="fa fa-trash"></i></button>';

            if ($('#users_table').val() == "") {
                currentTable = $('#users_table').DataTable();
            
                console.log(data);
                data.forEach(function(user){
                    currentTable.row.add([
                        user.contact_name,
                        user.lastname,
                        user.username,
                        user.tpname,
                        editDeleteBtnTemplate.replace("\{id\}", user.code).replace("\{id\}", user.code)
                    ]).draw( false );
                });

            }

            $('#users_table tbody').on('click', 'button.edit_user', function () {
                var currentUser = $(this);
                var editUserModal = $("#edit_user");

                var callback = function (data, status) {
                    console.log(data);
                    editUserModal.find("#username").val(data[0].username);
                    editUserModal.find("#type").val(data[0].usrtype).trigger("change");
                };
                var data_={"classname": "login.Get", "code":parseInt(currentUser.attr("data-id"))};
                console.log(data_);
                sugelico.getServerCall(data_, callback);

                var editUserCallback = function(data, status){
                    var form = editUserModal.find("#edit_user_form");
                }

                $("#edit_user_btn").click(function(){
                    formData = new FormData(document.getElementById("edit_user_form"));
                    formData.append("classname", "login.Handle");
                    formData.append("code", parseInt(currentUser.attr("data-id")));
                    console.log(formData);
                    sugelico.postFormServerCall(formData, function(data, status){

                        if (data.code>0){
                            $("#error_alert").addClass("hidden");
                            $("#success_alert").removeClass("hidden");
                            location.reload();
                            $("#edit_product").modal('toggle');
                        }else {
                            $("#error_alert").removeClass("hidden");
                            $("#success_alert").addClass("hidden");
                            console.log(data)
                        }
                    });
                });
            });
            $("#username").blur(function(event){
                var data = {
                    "classname": "login.confirmUsername",
                    "username": $("#username").val()
                };

                $.post("/", data, function(data, status){
                    $("span.form-control-feedback").css("display", "block");

                    if(data.response==1){
                        $("#username").parent().removeClass("has-success");
                        $("#username").parent().addClass("has-error").addClass("has-feedback");

                        $("span.form-control-feedback.glyphicon-ok").css("display", "none");
                        $("span.form-control-feedback.glyphicon-remove").css("display", "block");

                        $("#edit_user_btn").prop("disabled", true);

                    } else {
                        $("#username").parent().removeClass("has-error");
                        $("#username").parent().addClass("has-success").addClass("has-feedback");

                        $("span.form-control-feedback.glyphicon-remove").css("display", "none");
                        $("span.form-control-feedback.glyphicon-ok").css("display", "block");
                        $("#edit_user_btn").prop("disabled", false);
                    };
                });
            });
            $('#users_table tbody').on('click', 'button.delete_user', function () {
                deleteModuleBtnClicked($(this));
            });
        }
    }

    var data = {
        "classname": "login.Get"
    }

    sugelico.getServerCall(data, getUserCallBack);


    if ($("#add_user_form").length > 0) {
        var data = {
            "classname": "Types.Get",
            "level": 7
        }
        sugelico.getServerCall(data, function(data, status){
            var type_options = '<option value="">Seleccione tipo</option>';

            data.forEach(function(user_type){
                type_options += '<option value="'+ user_type.code +'">'+ user_type.tpname +'</option>';
            });

            $("#usrtype").html(type_options);
        });

        var data = {
            "classname": "login.getUsersBy",
            "usertype": 73
        }
        sugelico.getServerCall(data, function(data, status){
            var type_options = '<option value="">Seleccione mesero</option>';

            data.forEach(function(user_type){
                type_options += '<option value="'+ user_type.code +'">'+ user_type.name +'</option>';
            });

            $("#waiter_code").html(type_options);
        });
        $("#username").blur(function(event){
            var data = {
                "classname": "login.confirmUsername",
                "username": $("#username").val()
            };

            $.post("/", data, function(data, status){
                $("span.form-control-feedback").css("display", "block");

                if(data.response==1){
                    $("#username").parent().removeClass("has-success");
                    $("#username").parent().addClass("has-error").addClass("has-feedback");

                    $("span.form-control-feedback.glyphicon-ok").css("display", "none");
                    $("span.form-control-feedback.glyphicon-remove").css("display", "block");

                    $("#add_user_btn").prop("disabled", true);

                } else {
                    $("#username").parent().removeClass("has-error");
                    $("#username").parent().addClass("has-success").addClass("has-feedback");

                    $("span.form-control-feedback.glyphicon-remove").css("display", "none");
                    $("span.form-control-feedback.glyphicon-ok").css("display", "block");
                    $("#add_user_btn").prop("disabled", false);
                };
            });
        });
    }

    // Add user
    $("#add_user_form").submit(function (event) {
        event.preventDefault();
        if ($("#passwd").val()!==$("#repassword").val()){
            alert("Contraseñas son distintas");
            return;
        }
        formData = new FormData(document.getElementById("add_user_form"));
		formData.append("classname", "login.UserRegistration");
		formData.append("status", 11);
		sugelico.postFormServerCall(formData, function(data, status){

            console.log(data);
			if (data.value.code) {
				document.getElementById("add_user_form").reset();
			} else {
                console.log(data)
                $("#error_alert").toggle();
			}
		});
    });
    // Edit user
    $(".edit_user").click(function () {

    });


    $(".delete_user").click(function () {
        var currentUser = $(this).data("id");
        var deleteUserModal = $("#delete_user");

        var deleteUserCallback = function(data, status){
            console.log("eliminado");
        }

        $("#delete_user_btn").click(function(){
            deleteUserModal.modal("hide");
            var data = {
                "classname":"Users.Handle",
                "status":13, 
                "code": currentUser
            }
            sugelico.postServerCall(data, deleteUserCallback);
        });
    });
});