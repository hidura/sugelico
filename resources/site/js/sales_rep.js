$(function () {

	var data = {
        "classname": "Types.Get",
        "level": 4
    }
    sugelico.getServerCall(data,
        function(data, status){
        var type_options = '<option value="">Seleccione un tipo de producto</option>';

        data.forEach(function(category_type){
            type_options += '<option value="'+ category_type.code +'">'+ category_type.tpname +'</option>';
        });

        $("#product_type").html(type_options);
    }
    );
	//Type of product
	var data = {
        "classname": "Types.Get",
        "level": 13
    }
    sugelico.getServerCall(data,
        function(data, status){
        var type_options = '<option value="">Seleccione un tipo de producto</option>' +
            '<option value="0">Todos</option>';

        data.forEach(function(category_type){
            type_options += '<option value="'+ category_type.code +'">'+ category_type.tpname +'</option>';
        });

        $("#produ_type").html(type_options);
    }
    );



    var data = {
        "classname": "Categories.Get",
        "cat_name": ""
    }
    sugelico.postServerCall(data, function(data, status){
        var product_options = '<option value="">Seleccione una categoria</option>' +
            '<option value="0">Todo</option>';

        data.forEach(function(product_type){
            product_options += '<option value="'+ product_type.code +'">'+ product_type.cat_name+'</option>';
        });

        $("#category").html(product_options);
    });


    $("#filters").submit(function(event){
    	event.preventDefault();
    	var data = {
	        "classname": "Bills.GetSales",
	        "item_type": $("#product_type").val(),
	        "type_product": $("#produ_type").val(),
	        "category": $("#category").val(),
	        "end": $("#end").val(),
	        "from": $("#from").val()
	    };

	    console.log(data);

    	sugelico.postServerCall(data, function(data, status) {
    	    console.log(data);
			var currentTable = $('#sales_rep_table').DataTable();
            currentTable.clear().draw();
			data.forEach(function(product){
                currentTable.row.add([product.item_name, product.unit_name,
                    0.00,//(parseFloat(product.amount)-product.buys_amount)+product.sale_amount,
                    product.buys_amount, product.sale_amount,
                    parseFloat(product.amount),
                    sugelico.numberWithCommas((parseFloat(product.sale_amount)*parseFloat(product.price)).toFixed(2))]).draw( false );
            });
		});
    });
});