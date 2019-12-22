$(document).ready(function() {

    //GET ALL PRINTERS
    var getAllPrintersCallback = function(data, status) {
        data = JSON.parse(data);
        var currentTable;
        var editDeleteBtnTemplate = '<button class="btn btn-success edit_printer left" data-id="\{id\}" data-toggle="modal" data-target="#edit_printer"><i class="glyphicon glyphicon-pencil"></i></button>' +
                                    '<button class="btn btn-default delete_printer" data-id="\{id\}" data-toggle="modal" data-target="#delete_printer"><i class="glyphicon glyphicon-remove"></i></button>';
        
        if ($('#printers_table').val() == "") {
            currentTable = $('#printers_table').DataTable();
        }

        data.forEach(function(printer){
            currentTable.row.add([
                printer.brand,
                printer.model,
                "",
                "",
                "",
                printer.path,
                editDeleteBtnTemplate.replace("\{id\}", printer.code).replace("\{id\}", printer.code)
            ]).draw( false );
        });

        $('#printers_table tbody').on('click', 'button.edit_printer', function () {
            editModuleBtnClicked($(this));
        });

        $('#printers_table tbody').on('click', 'button.delete_printer', function () {
            deleteModuleBtnClicked($(this));
        } );
    }

    var data = {
        "classname": "General.getPrinters",
        "brand": ""
    }
    sugelico.getServerCall({"classname": "Company.Get","_name": ""}, function(data, status){
		cont =0;
		data.forEach(function(company){
			$("#company").append($('<option />').val(company.code).html(company._name));
		});

	});
    sugelico.getServerCall({"classname": "Types.Get","level": 14}, function(data, status){
		cont =0;
		data.forEach(function(type){
			$("#_type").append($('<option />').val(type.code).html(type.tpname));
		});

	});
    sugelico.getServerCall(data, getAllPrintersCallback);
    $("#printer_add_form").submit(function(event){
        event.preventDefault();
        formData = new FormData(document.getElementById("printer_add_form"));
        formData.append("classname", "General.HandlePrinter");
        formData.append("status", 11);

        sugelico.postFormServerCall(formData, function(data, status){

            if (data.code>0){
                window.location="/?md=printer_add"
            }else {
                $("#error_alert").removeClass("hidden");


            }

        });
    });

    // EDIT PRINTERS
    $(".edit_printer").click(function () {
        var currentPrinter = $(this);
        var editPrinterModal = $("#edit_printer");

        var callback = function(data, status){
            console.log(data);
            console.log(status);
            editPrinterModal.find("#brand").val("Printer 1");
            editPrinterModal.find("#model").val("CJSK-23a32-DD");
            editPrinterModal.find("#papersize").val("Activa");
            editPrinterModal.find("#thermal").val("1").trigger("change");
            editPrinterModal.find("#autocut").val("0").trigger("change");
            editPrinterModal.find("#path").val("72.wd.23.2323");
        }

        sugelico.getServerCall({}, callback);

        var editPrinterCallback = function(data, status){
            var form = editPrinterModal.find("#edit_printer_form");
            console.log(form.serialize());
        }

        $("#edit_printer_btn").click(function(){
            sugelico.postServerCall({}, editPrinterCallback);
        });
    });

    $(".delete_printer").click(function () {
        var currentPruductType = $(this);
        var deletePrinterModal = $("#delete_printer");

        var deletePrinterCallback = function(data, status){
            console.log("eliminado");
        }

        $("#delete_printer_btn").click(function(){
            deletePrinterModal.modal("hide");
            var data = {
                "classname":"Users.Handle",
                "status":13, 
                code:14
            }
            sugelico.postServerCall(data, deletePrinterCallback);
        });
    });
});