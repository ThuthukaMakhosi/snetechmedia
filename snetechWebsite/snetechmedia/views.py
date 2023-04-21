from django.shortcuts import render
from .models import News
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    """This method will be used to direct the user to the home page

        :returns: Home page

        :rtype: html
    """
    new = News.objects.all()
    return render(request, "home.html", {'new': new} )

@login_required
def gallery(request):
    return render(request, "gallery.html")

def artists(request):
    return render(request, "ourartists.html")

def contact(request):
    return render(request, "contactus.html")

 
