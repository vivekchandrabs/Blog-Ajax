function logout(){

	let csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val()

	var json_data = {}
	json_data["csrfmiddlewaretoken"] = csrfmiddlewaretoken

	$.ajax({
		url: '/signout/',
		type: "POST",
		dataType: "json",
		data: json_data,
		success: function(response){
			window.location = "/"
		}

	})
}