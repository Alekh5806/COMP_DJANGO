from django.shortcuts import render

# Create your views here.

# here we are going to write the views for our tweet app, we will have a view for the home page, and a view for the tweet detail page. 

def index(request):
    return render(request, 'tweet/index.html')

