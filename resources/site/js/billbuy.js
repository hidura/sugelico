var products=[];
$(function () {
    //Putting the
    var now = new Date();
    var month = (now.getMonth() + 1);
    var day = now.getDate();
    if (month < 10)
        month = "0" + month;
    if (day < 10)
        day = "0" + day;
    var today = now.getFullYear() + '-' + month + '-' + day;
    $("#generated").val(today);
    $("#payalert").val(today);
    $("#expiration").val(today);

    //LOAD all Categories
	var getCategoryCallBack = function (data, status) {
		if(data){
            var category_options = '<option value="0">Seleccione un producto</option>';
            data.forEach(function(product){
                category_options += '<option value="'+ product.code +'" ' +
                    'data="'+product.subtotal+';'
                    +product.tax+'">'+ product.item_name+'</option>';
            });

            $("#product").html(category_options);
        }
	};

	var data = {
        "classname": "Items.Get"
    };

	sugelico.postServerCall(data, getCategoryCallBack);

	var getNCFTypesCallBack = function (data, status) {
		if(data){
            var category_options = '<option value="0">Seleccione un Tipo de NCF</option>';

            data.forEach(function(ncftype){
                category_options += '<option value="'+ ncftype.code +'" ' +
                    '>'+ ncftype.name+'</option>';
            });

            $("#ncftype").html(category_options);
        }
	};


	sugelico.postServerCall({
        "classname": "Accounts.getNCFTypes",
        "name":""
    }, getNCFTypesCallBack);


	var getPayTypesCallBack = function (data, status) {
	    if(data){
            var category_options = '<option value="0">Seleccione un Tipo de pago</option>';

            data.forEach(function(paytype){
                category_options += '<option value="'+ paytype.code +'" ' +
                    '>'+ paytype.tpname+'</option>';
            });

            $("#paytype").html(category_options);
        }
	};


	sugelico.postServerCall({
        "classname": "Types.Get",
        "level":11
    }, getPayTypesCallBack);


	var getClientCallBack = function (data, status) {

	    if(data){
            var category_options = '<option value="0">Seleccione un Suplidor</option>';

            data.forEach(function(client){
                category_options += '<option value="'+ client.code +'" ' +
                    '>'+ client.sup_name+'</option>';
            });

            $("#supplier").html(category_options);
            $("#supplier").val(0).trigger("change");
        }
	};


	sugelico.postServerCall({
        "classname": "supplier.Get",
        "sup_name":""
    }, getClientCallBack);




	$("#add_product").click(function (event) {

        if($("#amount").val().length===0)
        {
            alert("Debe colocar una cantidad");
            return;
        }
        var amount=parseFloat($("#amount").val());
        var discount=0.00;


        var e = document.getElementById("product");
        var product_info = e.options[e.selectedIndex].getAttribute("data");
        var product_name = e.options[e.selectedIndex].text;
        var product_id = e.options[e.selectedIndex].value;
        var subtotal=parseFloat($("#subtotal_item").val());

        var tax=parseFloat($("#prod_tax").val());
        var item_total=parseFloat($("#prod_total").val());
        var currentTable = $('#products_bill').DataTable();
        var editDeleteBtnTemplate = '<button class="btn btn-default delete_user" ' +
            'data-id="\{id\}" data-target="#delete_product"><i ' +
            'class="fa fa-trash"></i></button>';
        products.push({"amount":amount, "product":product_id,
        "total_tax":tax,"subtotal":subtotal,"total":item_total});
        currentTable.row.add([product_name,sugelico.numberWithCommas(amount),
            sugelico.numberWithCommas(parseFloat(product_info.split(";")[0])),
        sugelico.numberWithCommas(subtotal),0.00,
            sugelico.numberWithCommas(tax),sugelico.numberWithCommas((item_total)),
            editDeleteBtnTemplate.replace("\{id\}", product_id)]).draw( false );
        $("#product").val(0).trigger("change");
        $("#amount").val("");
        $("#subtotal_item").val("");
        $("#prod_tax").val("");
        $("#prod_total").val("");
        var gen_subtotal=subtotal+parseFloat(sugelico.numberWithOutCommas($("#subtotal").text()));

        $("#subtotal").text(sugelico.numberWithCommas(gen_subtotal));

        $("#tax").text(sugelico.numberWithCommas(tax+parseFloat(sugelico.numberWithOutCommas($("#tax").text()))));
        $("#total").text(sugelico.numberWithCommas((subtotal+tax)+parseFloat(sugelico.numberWithOutCommas($("#total").text()))));
    });
});

function saveBill(target) {
    if ($("#subtotal").val().length<=0){
        alert("Debe colocar el subtotal, sino tiene coloque 0");
        return;
    }
    if ($("#taxes").val().length<=0){
        alert("Debe colocar el impuesto, sino tiene coloque 0");
        return;
    }
    if ($("#other_costs").val().length<=0){
        alert("Debe colocar los otros costos, sino tiene coloque 0");
        return;
    }
    if ($("#discount").val().length<=0){
        alert("Debe colocar el descuento, sino tiene coloque 0");
        return;
    }
    if ($("#total").val().length<=0){
        alert("Debe colocar el descuento, sino tiene coloque 0");
        return;
    }


    var data= {
        supplier:$("#supplier").val(),
        ncf:$("#ncf").val(),
        reference:$("#reference").val(),
        generated:$("#generated").val(),
        expires:$("#expiration").val(),
        payalert:$("#payalert").val(),
        paytype:$("#paytype").val(),
        subtotal:$("#subtotal").val(),
        total:$("#total").val(),
        other_costs:$("#other_costs").val(),
        discount:$("#discount").val(),
        credit:$("#credit:checked").length > 0,
        taxes:$("#taxes").val(),
        "classname":"Accounting.Handle",
        "products":JSON.stringify(products)
    };
    console.log(data);
    var success = function (data, status) {
        if (data.code!=undefined){
            document.getElementById("formulary").reset();
            var currentTable = $('#products_bill').DataTable();
            products=[];
            currentTable.clear().draw();
        }
    };
    $.ajax({
            url: sugelico.route,
            data: JSON.stringify(data),
            processData: false,
            contentType: 'application/json',
            type: 'POST',
            success: success
        }
    );

}
