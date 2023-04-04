from django.shortcuts import render

# Create your views here.


def showPage(request):
    return render(
        request,
        'app_control/page_main.html',
    )