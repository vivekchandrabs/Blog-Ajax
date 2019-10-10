from django.urls import path

from blogapp.views import get_all_posts, make_post, delete_post, signin, signup

urlpatterns = [
   path("login/",  signin),
   path("all-posts/", get_all_posts),

   path("make-post/", make_post),

   path("delete-post/<int:post_id>/", delete_post),


   path("signup/", signup),

]