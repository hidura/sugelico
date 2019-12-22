$(function () {
	$("#do_login").click(function(event){
		event.preventDefault();

		var data = {
			"classname": "login.LoginSys",
			"username": $("#emailaddress").val(),
			"passwd": $("#passwd").val()
		}

		var callback = function(data, status){
			console.log(data);
			if (data.key != undefined) {
				var d = new Date();
		        d.setTime(d.getTime() + (7*24*60*60*1000));
		        var expires = "expires="+ d.toUTCString();
		        document.cookie = "loginkey" + "=" + data.key + ";" + expires + ";path=/";
				window.location.href = "/?md=index";
			}else {
				alert("Nombre de usuario o contraseñas invalidos");
			}
		};

		sugelico.postServerCall(data, callback);
	});
});