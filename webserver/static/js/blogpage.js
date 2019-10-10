$(document).ready(function() {
    viewAllPosts();
});

function viewAllPosts() {  
    $.ajax({
        url: '/api/all-posts/',
        type: 'application/json',
        method: 'GET',
        success: function(response) {
            console.log(posts);
            for(let post of response.posts){
                // console.log(post);
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
// console.log("CSRF:" + $('[name="csrfmiddlewaretoken"]').val());


$("#makepost").click(function() {
    $.ajax({
        url: '/api/make-post/',
        type: 'POST',
        dataType: "json",
        data: {
            "csrfmiddlewaretoken": $('[name="csrfmiddlewaretoken"]').val(),
            "title": $("#blogtitle").val(),
            "content": $("#content").val()
        },
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
        url: `/api/delete-post/${post_id}/`,
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