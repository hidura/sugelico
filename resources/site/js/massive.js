function uploadFile(target){
    var fd = new FormData(document.getElementById("formulary_prods"));
    fd.append("classname", "Items.upload_massive");
    fd.append("code",$("#code").val());
    $.ajax({
            url: '/',
            data: fd,
            processData: false,
            contentType: false,
            type: 'POST',
            success: function(data){

                console.log(data);

            }
        }
    );
}
