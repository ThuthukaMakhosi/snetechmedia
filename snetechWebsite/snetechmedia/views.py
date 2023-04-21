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
    """This method will be used to direct the user to the gallery page. Can only be accessed if a user is logged in.

        :returns: Gallery page

        :rtype: html
    """
    return render(request, "gallery.html")

def artists(request):
    """This method will be used to direct the user to the artists page

        :returns: Artists page

        :rtype: html
    """
    return render(request, "ourartists.html")

def contact(request):
    """This method will be used to direct the user to the contacts page

        :returns: Contact Us page

        :rtype: html
    """
    return render(request, "contactus.html")

 
