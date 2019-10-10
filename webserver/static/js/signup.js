function signup(){
    let username = $("#username").val()
    let email = $("#email").val()
    let password = $("#password").val()
    let csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val()

    let json_data = {}
    json_data["username"] = username
    json_data["email"] = email
    json_data["password"] = password
    json_data["csrfmiddlewaretoken"] = csrfmiddlewaretoken

    $.ajax({
        url: "/api/signup/",
        method: "POST",
        type: "application/json",
        data: json_data,
        success: function(response){
            window.location = "/"
        }
    })
}

