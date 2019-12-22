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
			// window.location.href = "/?md=index";
		}

		sugelico.postServerCall(data, callback);
	});
});