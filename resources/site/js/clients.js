$(document).ready(function() {


    $("#add_supplier").submit(function(event){
        event.preventDefault();
        $("#add_client_btn").prop("disabled", true);

        var data = {
            "classname": "Clients.create",
            "cl_name": $("#client_name").val(),
            "rnc": $("#client_rnc").val(),
            "price": $("#client_price").val(),
            "telephone": $("#client_tel").val(),
            "_address": $("#client_address").val(),
            "credit": $("#client_credit").val()
        };

        sugelico.postServerCall(data, function(data, status){
            console.log(data);
            if (data.code) {
                window.location.reload();
            } else{
                $("#add_client_btn").prop( "disabled", false);
            }
        });
    });

    // SHOW ALL
    var getAllSuppliersCallback = function(data, status) {
        var currentTable;
        var editDeleteBtnTemplate = '<button class="btn btn-success edit_supplier left" data-id="\{id\}" ' +
            'data-toggle="modal" data-target="#edit_supplier"><i class="fa fa-pencil"></i></button>' +
                                    '<button class="btn btn-default delete_supplier" ' +
            'data-id="\{id\}" data-toggle="modal" data-target="#delete_supplier">' +
            '<i class="fa fa-remove"></i></button>';

        if ($('#suppliers_table').val() == "") {
            currentTable = $('#suppliers_table').DataTable();

            data.forEach(function(supplier){
                currentTable.row.add([
                    supplier.code,
                    supplier.cl_name,
                    supplier.rnc,
                    supplier.credit,
                    supplier.price,
                    editDeleteBtnTemplate.replace("\{id\}", supplier.code).replace("\{id\}", supplier.code)
                ]).draw( false );
            });
        }

        $('#suppliers_table tbody').on('click', 'button.edit_supplier', function () {
            editSupplierBtnClicked($(this));
        });

        $('#suppliers_table tbody').on('click', 'button.delete_supplier', function () {
            deleteSupplierBtnClicked($(this));
        } );
    }

    var data = {
        "classname": "Clients.Get",
        "cl_name": ""
    }

    if ($('#suppliers_table').val() == "") {
        sugelico.getServerCall(data, getAllSuppliersCallback);
    }

	// EDIT SUPPLIER
    $(".edit_supplier").click(function () {
        var currentSupplierGroup = $(this);
        var editSupplierModal = $("#edit_supplier");

        var callback = function(data, status){
        	console.log(data);
            console.log(status);
            editSupplierModal.find("#supplier_name").val("Juan Arias");
            editSupplierModal.find("#supplier_email").val("jaun_el_real@dminio.com");
            editSupplierModal.find("#supplier_tel").val("809-000-0000");
            editSupplierModal.find("#supplier_address").val("Lejisimo");
        }

        sugelico.getServerCall({}, callback);

        var editSupplierCallback = function(data, status){
			var form = editSupplierModal.find("#edit_supplier_form");
            console.log(form.serialize());
        }

        $("#edit_supplier_btn").click(function(){
            sugelico.postServerCall({}, editSupplierCallback);
        });
    });

    $(".delete_supplier").click(function () {
        var currentUser = $(this);
        var deleteSupplierModal = $("#delete_supplier");

        var deleteSupplierCallback = function(data, status){
            console.log("eliminado");
        }

        $("#delete_supplier_btn").click(function(){
            deleteSupplierModal.modal("hide");
            var data = {
                "classname":"Users.Handle",
                "status":13,
                code:14
            }
            sugelico.postServerCall(data, deleteSupplierCallback);
        });
    });
});