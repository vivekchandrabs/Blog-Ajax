from django.urls import path

from webserver.views import signup, blogpage

urlpatterns = [
   path("signup/", signup),
   path("", blogpage),

]