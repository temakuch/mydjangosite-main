from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
def show_posts(request):
	if request.method == "GET":
		res = post.objects.all()
		context = {'posts': res}
		return render(request, 'post_list.html', context)
def show_shrek(request):
	if request.method == "GET":
		return HttpResponse('<a href="https://www.youtube.com/watch?v=P0BL0gc006w">SHREK</a>')
	
def show_one_post(request, post_id):
	_post = get_object_or_404(post, id = post_id)
	context = {'post' : _post}
	return render(request, 'one_post.html', context)

def register(request):
	err = ''
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/blog")
		else:
			err = form.errors.as_data()	
	form = UserCreationForm
	context = {"form": form, 'error':err}
	return render(request, 'register.html', context)

