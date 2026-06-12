from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
# Create your views here.

# here we are going to write the views for our tweet app, we will have a view for the home page, and a view for the tweet detail page. 

def index(request):
    return render(request, 'index.html')

def tweet_detail(request,tweet_id):
    # here we will get the tweet data from the database using the id of the tweet and then we will pass the data to the template and show the tweet detail page to the user.
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_detail.html', {'tweet_id':tweet_id})

# now we will write the views for creating new tweets using the if- else statement if the user has send the fillen form and in else we will handle to fill the form and send it to the template.
# get will be used to fill the form and post will be used to send the form data to the server and save it in the database.
def create_tweet(request):
    if (request.method == 'POST'):
        form = TweetForm(request.POST , request.FILES)
        # now we will check the user is valid or not if the form is valid then we will save the form data in the database and if the form is not valid then we will pass it to the template and show the error message to the user.
        #and with the request we get the user so we will save the user in the database with the tweet data.
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            #now we will redirect the user to the tweet detail page after creating the tweet.
            return redirect('tweet_detail', tweet_id = tweet.id)
    else:
        form = TweetForm()
    return render(request , 'create_tweet.html', {'form' : form})

# now we will write a view to edit the tweet , using the id of the tweet we will get the tweet data from the database and fill the form with the data and then we will save the data in the database after editing it.the get method will be used to fill the form with the data and the post method will be used to send the edited data to the server and save it in the database.
def edit_tweet(request, tweet_id):
    # by using the get_object_or_404 method we will get the tweet data from the database and if the tweet is not found then it will return a 404 error page.and we will also check if the user is the owner of the tweet or not if the user is not the owner of the tweet then we will return a 404 error page.
    tweet = get_object_or_404(Tweet, id=tweet_id, user = request.user)
    if (request.method == 'POST'):
        form = TweetForm(request.POST , request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_detail', tweet_id = tweet.id)
    else:
        form = TweetForm(instance=tweet)
    return render(request , 'edit_tweet.html', {'form' : form})

# now we will write a view to delete the tweet, using the id of the tweet we will get the tweet data from the database and then we will delete the tweet data from the database and then we will redirect the user to the home page after deleting the tweet.
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user = request.user)
    if (request.method == 'POST'):
        tweet.delete()
        return redirect('index')
    return render(request , 'delete_tweet.html', {'tweet' : tweet})
    
