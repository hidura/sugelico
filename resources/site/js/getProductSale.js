$(function () {
	var gen607ReportCallback = function(data, status) {
	    console.log(data);
	    if (data.error===undefined){
            var currentTable = $('#gen607_table').DataTable();

            currentTable.clear().draw();
            // data.details.forEach(function(bill){
            //     console.log(bill);
            //     currentTable.row.add([
            //         bill.bill_date,
            //         bill.client_name,
            //         bill.rnc,
            //         (bill.ncf===null || bill.ncf===undefined) ?"" :bill.ncf,
            //         sugelico.numberWithCommas(parseFloat(bill.billsubtotal).toFixed(2)),
            //         sugelico.numberWithCommas(parseFloat(bill.billtax).toFixed(2)),
            //         sugelico.numberWithCommas(parseFloat(bill.billtotal).toFixed(2)),
            //         bill.ptpayname
            //     ]).draw( false );
            // });
        }

	};



    var data = {
        "classname": "Bills.getProductsSale",
        "end_date": $("#end").val(),
        "ncf_type":$("#ncftype").val(),
        "from_date": $("#from").val()
    }
    sugelico.postServerCall(data, gen607ReportCallback);
});