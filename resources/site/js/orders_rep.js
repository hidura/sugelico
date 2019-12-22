$(function () {

    $("#filters").submit(function(event){
    	event.preventDefault();

    	var data = {
	        "classname": "Bills.getProdsHistPreorder",
	        "preorder": $("#order").val()
	    }

	    console.log(data);

    	sugelico.postServerCall(data, function(data, status) {
			console.log(data);
		});
    });
});