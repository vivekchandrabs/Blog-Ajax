from django.urls import path

from blogapp.views import get_all_posts, get_all_post_comments, make_post, delete_post, make_comment, delete_comment

urlpatterns = [
   path("all-posts/", get_all_posts),
   path("all-comments/<int:post_id>/", get_all_post_comments),

   path("make-post/", make_post),

   path("delete-post/<int:post_id>/", delete_post),

   path("make-comment/<int:post_id>/", make_comment),

   path("delete-comment/<int:comment_id>/", delete_comment),

]