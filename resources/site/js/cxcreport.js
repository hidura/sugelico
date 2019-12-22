var tableTitle="CUENTAS X COBRAR";
printableColumns=[0,1,2,3,4,5,6];
$(function () {
	var gen607ReportCallback = function(data, status) {
        if (data.error===undefined){
            var currentTable = $('#cxctable').DataTable({
            "language": {
                "lengthMenu": "Mostrar _MENU_ registros por pagina",
                "zeroRecords": "No se encontraron registros. Verificar que el text esta bien escrito.",
                "info": "Mostrando pagina _PAGE_ of _PAGES_",
                "infoEmpty": "No hay registros disponibles.",
                "infoFiltered": "(De _MAX_ registros existentes.)",
                "search": "Buscar",
                "paginate": {
                    "first": "Primero",
                    "last": "Último",
                    "next": "Siguiente",
                    "previous": "Anterior"
                }
            },
            dom: 'B<"clear">lfrtip',
            buttons: {
                name: 'primary',
                buttons: [
                    'copy', 'csv', 'excel',
                    {
                        extend: 'pdf',
                        title: tableTitle,
                        text: 'PDF',
                        footer:true,
                        exportOptions: {
                            columns: printableColumns

                        }
                    },
                    {
                        extend: 'print',
                        title: tableTitle,
                        text: 'Print',
                        autoPrint: true,
                        footer:true,
                        exportOptions: {
                            columns: printableColumns
                        }
                    }
                ]
            },"footerCallback":
                    function ( row, data, start, end, display ) {
                var api = this.api(), data;

                // Remove the formatting to get integer data for summation
                var intVal = function ( i ) {
                    return typeof i === 'string' ?
                        i.replace(/[\$,]/g, '')*1 :
                        typeof i === 'number' ?
                            i : 0;
                };

                // Total over all pages
                subttotal = api
                    .column( 4 )
                    .data()
                    .reduce( function (a, b) {
                        return intVal(a) + intVal(b);
                    }, 0 );
                // Total over this page
                pageSubTotal = api
                    .column( 4, { page: 'current'} )
                    .data()
                    .reduce( function (a, b) {
                        return intVal(a) + intVal(b);
                    }, 0 );
                $("#subtotal").text(sugelico.numberWithCommas(pageSubTotal.toString()));


                // Total over all pages
                tax = api
                    .column( 5 )
                    .data()
                    .reduce( function (a, b) {
                        return intVal(a) + intVal(b);
                    }, 0 );
                // Total over this page
                pageTax= api
                    .column( 5, { page: 'current'} )
                    .data()
                    .reduce( function (a, b) {
                        return intVal(a) + intVal(b);
                    }, 0 );

                // Update footer
                $("#tax").text(sugelico.numberWithCommas(pageTax.toString()));




                // Total over all pages
                total = api
                    .column( 6 )
                    .data()
                    .reduce( function (a, b) {
                        return intVal(a) + intVal(b);
                    }, 0 );
                // Total over this page
                pageTotal= api
                    .column( 6, { page: 'current'} )
                    .data()
                    .reduce( function (a, b) {
                        return intVal(a) + intVal(b);
                    }, 0 );

                // Update footer
                $("#total").text(sugelico.numberWithCommas(pageTotal.toString()));


            }

        });
            currentTable.clear().draw();
            data.forEach(function(bill){
                currentTable.row.add([
                    new JulianDate().julian(bill.billdate).getDate().toLocaleDateString("en-US"),
                    bill.client_name,
                    bill.ordertype_name,
                    bill.billcode,
                    bill.billsubtotal,
                    bill.billtax,
                    bill.billtotal
                ]).draw( false );
            });
        }

	};



    $("#filters").submit(function(event){
    	event.preventDefault();
    	var data = {
	        "classname": "Bills.getCXCBills",
	        "end": $("#end").val(),
	        "from": $("#from").val()
	    }
    	sugelico.postServerCall(data, gen607ReportCallback);
    });
});