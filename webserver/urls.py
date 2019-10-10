from django.urls import path

from webserver.views import signup, blogpage, blogdetail

urlpatterns = [
   path("signup/", signup),

   path("", blogpage),

   path("blogdetail/", blogdetail),
]