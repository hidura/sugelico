var paytpdef={};
$(document).ready(function() {
    if ($('#paytype_table').val() == "") {
        var data = {
            "classname": "Accounts.getPayType"
        };
        sugelico.getServerCall(data, function(data, status) {
                var currentTable;
                var editDeleteBtnTemplate = '<a class="btn btn-success edit_category left" target="_blank" ' +
                    'href="/?md=paytypes_add&code=\{id\}" data-toggle="modal" ' +
                    'data-target="#edit_category"><i class="fa fa-pencil"></i></a>' +
                '<button class="btn btn-default delete_category" data-id="\{id\}" data-toggle="modal" ' +
                    'data-target="#delete_category"><i class="fa fa-trash"></i></button>';


                currentTable = $('#paytype_table').DataTable();
                currentTable.clear().draw();
                data.forEach(function (paytype) {
                    console.log(paytype);
                    currentTable.row.add([
                        paytype.tpname,
                        (paytype.paydetails[0]===undefined)? "" : (paytype.paydetails[0].reference===false?"NO":"SI" +
                            ""),
                        (paytype.paydetails[0]===undefined)? 0.00 :paytype.paydetails[0].percent_extra,
                        editDeleteBtnTemplate.replace("\{id\}", paytype.code).replace("\{id\}", paytype.code)
                    ]).draw(false);

                });

            });

	}

    if($('#paytypes_lst').val()===""){
        if (sugelico.getParameterByName("code")!==undefined){
            var data = {
                "classname": "Accounts.getPayType",
                "code":sugelico.getParameterByName("code")
            };
            sugelico.getServerCall(data, function(result, status) {
                result.forEach(function (data) {

                    $("#tpname").val(data.tpname);
                    $("#reference").val(data.paydetails[0] === undefined) ? -1 : (paytype.paydetails[0].reference === false ? 0 : 1);
                    $("#percent").val(data.paydetails[0].percent_extra);
                    var currentTable;
                    var editDeleteBtnTemplate =
                        '<button class="btn btn-default delete_category" ' +
                        'data-id="\{id\}" data-toggle="modal" data-target="#delete_category"><i ' +
                        'class="glyphicon glyphicon-remove"></i></button>';


                    currentTable = $('#paytypes_lst').DataTable();
                    currentTable.clear().draw();
                    paytpdef = data.paydetails[0].denomination;
                    for (var prop in paytpdef){
                        currentTable.row.add([
                            paytpdef[prop],prop,
                            editDeleteBtnTemplate.replace("\{id\}", prop)
                        ]).draw(false);
                    }
                    $(".delete_category").click(function (event) {

                        delete paytpdef[parseInt($(this).attr("data-id"))];
                        var obj = paytpdef;
                        currentTable = $('#paytypes_lst').DataTable();
                        currentTable.clear().draw();
                        for (var prop in obj){
                            currentTable.row.add([
                                obj[prop],prop,
                                editDeleteBtnTemplate.replace("\{id\}", prop)
                            ]).draw(false);
                        }
                    })
                });
            });

        }


        $('#paytypes_lst').DataTable();
        $("#add_payment").click(function (event) {
            var editDeleteBtnTemplate = '<button class="btn btn-default delete_product" action="delete" data-toggle="modal" data-target="#delete_product"><i class="glyphicon glyphicon-remove"></i></button>';

            var currentTable = $('#paytypes_lst').DataTable();
            var amount_lbl=$("#amount_lbl").val();
            var key_value=$("#key_value").val();
            if (!paytpdef.hasOwnProperty(key_value)){
                currentTable.row.add([
                    amount_lbl,
                    key_value,
                    editDeleteBtnTemplate
                ]).draw( false );
                paytpdef[key_value]=amount_lbl;
            }
            $("#amount_lbl").val("");
            $("#key_value").val("");
        });
        $("#save_paytp").click(function (event) {

            var data_send={
                tpname:$("#tpname").val(),
                paytplst:JSON.stringify(paytpdef),
                reference:$("#reference").val(),
                percent:$("#percent").val(),
                "classname":"Accounts.HandlePayType"
            };
            if (sugelico.getParameterByName("code")!==undefined){
                data_send["code"]=sugelico.getParameterByName("code")
            }
            sugelico.postServerCall(data_send, function(data, status){
                console.log(data);
                if (data.code>0){
                    window.location="/?md=paytypes_add"
                }

            });


        });
    }

});