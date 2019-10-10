var url = new URLSearchParams(window.location.search);

var post_id = url.get('id');
// console.log(post_id);

$.ajax({
    url: `/api/all-comments/${post_id}/`,
    type: 'application/json',
    method: 'GET',
    success: function(response) {
        // console.log(response.post.title);
        $('#blogpost').append(`
            <h2> ${response.post.title} </h2>
            <p><small> ${response.post.timestamp} </small></p>
            <p> ${response.post.content} </p>
        `);
        for(let comment of response.comments){
            // console.log(comment.post_id);
            $("#comments").append(`
                <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">${comment.content}</h5>
                            <p class="card-text">${comment.timestamp}</p>
                            <p class="card-text">${comment.author}</p>
                    </div>
                </div>
            `);
        };
    }
});

