from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
	return render(request, "index.html")


@login_required()
def error404(request):
	return render(request, "errors/404error.html")


@login_required()
def error500(request):
	return render(request, "errors/500error.html")
