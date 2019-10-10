$.ajax({
    url: '/api/all-posts/',
    type: 'application/json',
    method: 'GET',
    success: function(response) {
        console.log(posts);
        for(let post of response.posts){
            // console.log(post);
            $("#posts").append(`
                <div class="card" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title">${post.title}</h5>
                            <p class="card-text">${post.content}</p>
                            <p class="card-text">${post.timestamp}</p>
                    </div>
                </div>
            `);
        };
    }
});

