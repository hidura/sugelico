var products=[];
$(document).ready(function() {
    var currentTable = $('#products_lst').DataTable();
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

		$("#add_product").click(function (event) {

            if($("#amount").val().length===0)
            {
                alert("Debe colocar una cantidad");
                return;
            }
            var amount=parseFloat($("#amount").val());

            var e = document.getElementById("product");
            var product_name = e.options[e.selectedIndex].text;
            var product_id = e.options[e.selectedIndex].value;

            var currentTable = $('#products_lst').DataTable();
            var editDeleteBtnTemplate = '<button class="btn btn-default delete_user" onClick="delete_product(this);" ' +
                'data-id="\{id\}" data-toggle="modal"' +
                ' data-target="#delete_product"><i class="glyphicon glyphicon-remove"></i></button>';
            products.push({"amount":amount, "name":product_name,"product":product_id});
            currentTable.row.add([product_name,sugelico.numberWithCommas(amount),editDeleteBtnTemplate.replace("\{id\}", product_id)]).draw( false );
            $("#product").val(0).trigger("change");
            $("#amount").val("");

        });
});

function delete_product(target) {
    
}