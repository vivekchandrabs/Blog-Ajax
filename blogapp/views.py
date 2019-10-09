from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, logout, login
import json

from blogapp.models import Post, Comment
# Create your views here.

def signup(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		email = request.POST.get("email")

		user = User.objects.filter(username=username).exist()

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

	return JsonResponse({"error_message":f"{request.method} not allowed" }, status=403)


def post_to_dict(post_instance):
	post_data = {}
	post_data["id"] = post_instance.id
	post_data["title"] = post_instance.title
	post_data["content"] = post_instance.content
	post_data["timestamp"] = post_instance.timestamp

	return post_data

def comment_to_dict(comment_instance):
	comment_data = {}
	comment_data["id"] = comment_instance.id
	comment_data["content"] = comment_instance.content
	comment_data["timestamp"] = comment_instance.timestamp

	return comment_data

def get_all_posts(request):
	all_posts = Post.objects.all().values()
	return JsonResponse({"posts":list(all_posts)})

def get_all_post_comments(request, post_id):
	post_instance = Post.objects.get(pk=post_id)
	comment_instances = Comment.objects.filter(post=post_instance)
	post_data = post_to_dict(post_instance)

	return JsonResponse({"post":post_data, "comments":list(comment_instances.values())})

def make_post(request):
	title = request.POST.get("title")
	content = request.POST.get("content")

	post_instance = Post.objects.create(title=title,
										content=content)
	post_data = post_to_dict(post_instance)

	return JsonResponse({"post":post_data})

def delete_post(request, post_id):
	post_instance = Post.objects.get(pk=post_id)
	post_instance.delete()

	return JsonResponse({"message":"Post Successfully deleted"})


def make_comment(request, post_id):
	post_instance = Post.objects.get(pk=post_id)

	content = request.POST.get("content")
	
	comment_instance = Comment.objects.create(post=post_instance,
										content=content)

	comment_data = comment_to_dict(comment_instance)

	return JsonResponse({"comment":comment_data})

def delete_comment(request, comment_id):
	comment_instance = Comment.objects.get(pk=comment_id)
	comment_instance.delete()

	return JsonResponse({"message":"Successfully Deleted the Comment"})







