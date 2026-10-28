from django.shortcuts import render
def  home(request):
    context = {
        "app_name":"Task Tracker",
        "message":"Welcome"
    }
    return render(request,"home.html",context)
