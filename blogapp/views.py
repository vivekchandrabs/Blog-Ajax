from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
import json

from blogapp.models import Post
# Create your views here.

def signup(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		email = request.POST.get("email")

		user = User.objects.filter(username=username).exists()

		if not user:
			user = User.objects.create(username=username, 
										password=password, 
										email=email)
			login(request, user)

			return JsonResponse({"message":"User Created Successfully"})

		return JsonResponse({"error_message":"User Already exists"}, status=403)

	return JsonResponse({"error_message":f"{request.method} not allowed" }, status=403)


def signin(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)

			return JsonResponse({"message":"Successfully Loged in"})

		return JsonResponse({"error_message":"User Does not exists"}, status=404)

	return JsonResponse({"error_message":f"{request.method} not allowed" }, status=406)


def post_to_dict(post_instance):
	post_data = {}
	post_data["id"] = post_instance.id
	post_data["title"] = post_instance.title
	post_data["content"] = post_instance.content
	post_data["timestamp"] = post_instance.timestamp

	return post_data

def get_all_posts(request):
	if request.method == "POST":
		user = request.user
		all_posts = Post.objects.filter(author=user).values()

		return JsonResponse({"posts":list(all_posts)})

	return JsonResponse({"error_message":f"{request.method} not allowed" }, status=406)

def make_post(request):
	if request.method == "POST":
		title = request.POST.get("title")
		content = request.POST.get("content")
		print(request.user)
		user = request.user

		post_instance = Post.objects.create(title=title,
											content=content,
											author=user)
		post_data = post_to_dict(post_instance)

		return JsonResponse({"post":post_data})

	return JsonResponse({"error_message":f"{request.method} not allowed" }, status=406)



def delete_post(request, post_id):
	post_instance = Post.objects.get(pk=post_id)
	post_instance.delete()

	return JsonResponse({"message":"Post Successfully deleted"})


def signout(request):
	logout(request)
	return JsonResponse({"message":"Successfully logged out"})


def home(request):
    return render(request, "signup.html")

def blogpage(request):
    return render(request, "blogpage.html")
