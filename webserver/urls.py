from django.urls import path

from webserver.views import signin, signup, blogpage, blogdetail

urlpatterns = [
   path("signup/", signup),
   path("signin/", signin),

   path("", blogpage),

   path("blogdetail/", blogdetail),
]