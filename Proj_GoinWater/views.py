from django.shortcuts import render


def mainpage(request):
    return render(request, 'base_mainpage.html')
