from django.shortcuts import render, HttpResponse

# Create your views here.
def printres(request):
    return HttpResponse("<br><br><br><br><br><br><br><center><h1>Hello tanmay !! this is from production</h1><br><hr color='blue'></center>")