var labels=[];
var values=[];
var data=[];
$(function () {

    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = '/resources/site/assets/chart.js/dist/Chart.js';

    // Then bind the event to the callback function.
    // There are several events for cross browser compatibility.


    // Fire the loading
    head.appendChild(script);



    var url = "ws://erpta.sugelico.com:13267/api";

    if (!window.WebSocket) alert("WebSocket not supported by this browser");

    var myWebSocket = {
        connect: function () {
            var location = url;
            var full = window.location.host;
            //window.location.host is subdomain.domain.com
            var parts = full.split('.');

            this._ws = new WebSocket(location+"?keyses="+getCookie("loginkey"));

            this._ws.onopen = this._onopen;
            this._ws.onmessage = this._onmessage;
            this._ws.onclose = this._onclose;
            this._ws.onerror = this._onerror;

        },

        _onopen: function () {
            console.debug("WebSocket Connected");
        },

        _onmessage: function (message) {
            data = JSON.parse(message.data);
            console.log(data);
            if (data.error!=undefined){
                $("#error_msg").text(data.error);
                $("#msg_box").slideDown('fast');
                return;
            }
            // productSold=data.products_sale.slice(data.products_sale.length-7,data.products_sale.length);
            // labels=[];
            // values=[];
            // loadChart();
            // productSold.forEach(function (product) {
            //    labels.push(product[0]);
            //    values.push(product[1])
            // });
            // loadChart();
            // $("#daily_income").text("RD$"+sugelico.numberWithCommas(data.fulltotal));
            // $("#net_income").text("RD$"+sugelico.numberWithCommas(data.fullsubtotal));
            // $("#open_orders").text(sugelico.numberWithCommas(data.open_preorders));
            // console.log(data);
            // $("#paytypes").empty();
            // for (var key in data.paytypetotals) {
            //     var tblStr="<table><tbody>" +
            //
            //         "<tr>"+
            //             "<td>Total</td><td>"+sugelico.numberWithCommas(data.paytypetotals[key]["total"])+"</td>" +
            //         "</tr>" +
            //         "</tbody></table>"
            //     $("#paytypes").append("<div class='card' style='width: 18rem;'>\n" +
            //         "  <div class='card-body'>\n" +
            //         "    <h5 class='card-title'>"+key+"</h5>\n" +
            //         "    <p class='card-text'>"+tblStr+" </p>\n" +
            //         "    <a href='#' data-id='"+key+"' onClick='billsLst(this);' class='btn btn-primary'>Ver Más</a>\n" +
            //         "  </div>\n" +
            //         "</div>")
            // }

        },

        _onclose: function () {
            console.debug("WebSocket Closed");
        },

        _onerror: function (e) {
            console.debug("Error occured: " + e);
        },

        _send: function (message) {
            console.debug("Message Send: " + message);
            if (this._ws) this._ws.send(message);
        }
    };

    myWebSocket.connect();
    // Adding the script tag to the head as suggested before



});
function billsLst(target) {
    var tr="";
    data.bills.forEach(function (bill) {
        if ($(target).attr("data-id")===bill.paytpname){
            tr+="<tr>" +
                    "<td>" +bill.billpreorder+"</td>" +
                    "<td>" +sugelico.numberWithCommas(bill.ptpsubtotal)+"</td>" +
                    "<td>" +sugelico.numberWithCommas(bill.ptptax)+"</td>" +
                    "<td>" +sugelico.numberWithCommas(bill.ptptotal)+"</td>" +
                    "<td>" +sugelico.numberWithCommas(bill.ptpaid)+"</td>" +
                "</tr>"
        }
    });
    var tblStr="" +
        "<div class='col-md-12'>" +
            "<table class='table table-responsive'>" +
                "<thead>" +
                    "<tr>" +
                        "<td>Codigo</td>" +
                        "<td>Subtotal</td>" +
                        "<td>Impuesto</td>" +
                        "<td>Total</td>" +
                        "<td>Total pagado</td>" +
                    "</tr>" +
                "</thead>" +
                "<tbody>" +
                    tr+
                "</tbody>"+
            "</table>" +
        "</div>";
    sugelico.openDialog("Facturas",tblStr);
}
function loadChart() {
    var ctx = document.getElementById("bills");
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Productos mas vendidos',
                data: values,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}