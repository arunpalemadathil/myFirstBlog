from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# Create your views here.
def index(request):
    today=datetime.datetime.now().date()
    daysOfWeek=('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
    return render(request, 'music/index.html', {"today" : today.day, "days_of_week" : daysOfWeek})

def morning(request):
    return render(request, 'music/morning.html', {})

def viewArticle(request,articleId):
    text="Displaying Article Number: %s" %articleId
    return HttpResponse(text)

def viewArticles(request,month,year):
    text="Displaying articles of : %s/%s"%(year,month)
    return HttpResponse(text)

