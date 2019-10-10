from django.urls import path

from blogapp.views import *

urlpatterns = [

   path("", home),
   
   path("blog/", blogpage),

   path("login/",  signin),
   
   path("signup/", signup),

   path("all-posts/", get_all_posts),

   path("make-post/", make_post),

   path("delete-post/<int:post_id>/", delete_post),

   path("signout/", signout),

]