from django.shortcuts import render


def index(request):
    template = "ritm_style/index.html"
    return render(request, template)


def news(request):
    template = "ritm_style/news.html"
    return render(request, template)


def blog(request):
    template = "ritm_style/blog.html"
    return render(request, template)
