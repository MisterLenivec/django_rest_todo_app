from django.shortcuts import render


def front_list(request):
    return render(request, 'frontend/list.html')
