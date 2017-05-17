from django.shortcuts import render


def index(request):
    return render(request, 'faq/index.html')


def notice(request):
    return render(request, 'faq/notice.html')
