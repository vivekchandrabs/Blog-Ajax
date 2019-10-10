$(document).ready(function() {
    viewAllPosts();
});

function viewAllPosts() {  

    $.ajax({
        url: '/all-posts/',
        type: 'POST',
        dataType: 'json',
        data: {
            "csrfmiddlewaretoken":$('[name="csrfmiddlewaretoken"]').val()
        },
        success: function(response) {
            console.log(posts);
            for(let post of response.posts){
                $("#posts").append(`
                    <div class="col-md-4">
                        <div class="card text-white bg-primary mb-3" style="width: 18rem;">
                            <div class="card-header d-flex align-items-center justify-content-between">
                                <h5 class="card-title">${post.title}</h5>
                                <button type="button" style="padding: 5px 10px;" id="${post.id}" class="btn btn-outline-warning" onclick="deletePost(${post.id})">
                                    <span>x</span>
                                </button>
                            </div>
                            <div class="card-body">
                                <p class="card-text">${post.content}</p>
                                <p class="card-text">${post.timestamp}</p>
                            </div>
                        </div>
                        <br>
                    </div>
                `);
            };
        }
    });   
}

$("#makepost").click(function() {

    let json_data = {}
    json_data["csrfmiddlewaretoken"] = $('[name="csrfmiddlewaretoken"]').val()
    json_data["title"] =  $("#blogtitle").val()
    json_data["content"] = $("#content").val()

    $.ajax({
        url: '/make-post/',
        type: 'POST',
        dataType: "json",
        data: json_data,

        success: function(response) {
            console.log(response.post);
            $("#exampleModal").modal('hide');

            $("#posts").append(`

            <div class="col-md-4">
                    <div class="card text-white bg-primary mb-3" style="width: 18rem;">
                        <div class="card-header d-flex align-items-center justify-content-between">
                            <h5 class="card-title">${response.post.title}</h5>
                            <button type="button" style="padding: 5px 10px;" id="${response.post.id}" class="btn btn-outline-warning" onclick="deletePost(${response.post.id})">
                                <span>x</span>
                            </button>
                        </div>
                        <div class="card-body">
                            <p class="card-text">${response.post.content}</p>
                            <p class="card-text">${response.post.timestamp}</p>
                        </div>
                    </div>
                    <br>
                </div>
                
            `);
            
        }
    });
});


function deletePost(post_id) {
    // console.log("Clicked" + post_id);
    $.ajax({
        url: `/delete-post/${post_id}/`,
        type: "application/json",
        method: "GET",
        success: function(res) {
            // console.log("Deleted" + post_id);
            alert(res.message);
            $("#posts").empty();
            viewAllPosts();
        }
    }); 
}