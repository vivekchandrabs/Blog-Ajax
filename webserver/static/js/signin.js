function signin(){
    let username = $("#signin-username").val()
    let password = $("#signin-password").val()
    let csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val()

    let json_data = {}
    json_data["username"] = username
    json_data["password"] = password
    json_data["csrfmiddlewaretoken"] = csrfmiddlewaretoken
    console.log(json_data)

    $.ajax({
        url: "/api/login/",
        type: "POST",
        dataType: "json",
        data: json_data,
        success: function(response){
            window.location = "/"
        }
    });
}